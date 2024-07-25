use std::time::Duration;
use serde_json::Value;
use std::panic;
use crate::test_case::load_test_cases;
use crate::timer::panic_after;
use assert_float_eq::assert_float_relative_eq;

fn compare_general(result: &Value, expected: &Value) {
    if expected.is_f64() {
        assert_float_relative_eq!(result.as_f64().unwrap(), expected.as_f64().unwrap(), 1e-6);
        return;
    }
    if result.is_array() && !expected.is_array() {
        if let Some(result_array) = result.as_array() {
            assert_eq!(result_array.iter().next().unwrap(), expected);
            return;
        }
    }
    assert_eq!(result, expected);
}

pub fn run_test(problem_id: &str, problem_folder: &str, solve: fn(String) -> Value) {
    println!("Run [Problem {}] Test Cases", problem_id);
    let (inputs, expected_outputs) = load_test_cases(problem_folder, problem_id);
    panic_after(Duration::from_secs(10), move || {
        for i in 0..inputs.len() {
            let inputs_clone = inputs.clone();
            let expected_outputs_clone = expected_outputs.clone();
            panic_after(Duration::from_secs(5), move || {
                let result = solve(inputs_clone[i].to_string());
                let check = panic::catch_unwind(|| {
                    compare_general(&result, &expected_outputs_clone[i]);
                });
                if check.is_err() {
                    let mut iter_result = solve(inputs_clone[i].to_string());
                    if iter_result == result {
                        panic!("{:?}", check.err());
                    }
                    for j in 0..500 {
                        let iter_check = panic::catch_unwind(|| {
                            compare_general(&iter_result, &expected_outputs_clone[i]);
                        });
                        if iter_check.is_ok() {
                            return;
                        } else if j == 499 {
                            panic!("{:?}", iter_check.err());
                        }
                        iter_result = solve(inputs_clone[i].to_string());
                    }
                }
            });
        }
    });
}