use std::time::Duration;
use serde_json::Value;
use crate::test_case::load_test_cases;
use crate::timer::panic_after;

pub fn run_test(problem_id: &str, problem_folder: &str, solve: fn(String) -> Value) {
    println!("Run [Problem {}] Test Cases", problem_id);
    let (inputs, expected_outputs) = load_test_cases(problem_folder, problem_id);
    panic_after(Duration::from_secs(10), move || {
        for i in 0..inputs.len() {
            let inputs_clone = inputs.clone();
            let expected_outputs_clone = expected_outputs.clone();
            panic_after(Duration::from_secs(3), move || {
                let result = solve(inputs_clone[i].to_string());
                assert_eq!(result, expected_outputs_clone[i], "Test case {}: [{}]", i, inputs_clone[i].replace('\n', ", "));
            });
        }
    });
}