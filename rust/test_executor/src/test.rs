const PROBLEM_FOLDER: &str = "problems";
const PROBLEM_ID: &str = "2";

#[cfg(test)]
mod test {
    use std::time::Duration;

    use solution;
    use test_executor::{test_case::load_test_cases, timer::panic_after};

    use crate::{PROBLEM_FOLDER, PROBLEM_ID};

    #[test]
    fn test_solution() {
        println!("Run [Problem {}] Test Cases", PROBLEM_ID);
        let (inputs, expected_outputs) = load_test_cases(PROBLEM_FOLDER, PROBLEM_ID);
        panic_after(Duration::from_secs(10), move || {
            for i in 0..inputs.len() {
                let inputs_clone = inputs.clone();
                let expected_outputs_clone = expected_outputs.clone();
                panic_after(Duration::from_secs(3), move || {
                    let result = solution::solve(inputs_clone[i].to_string());
                    assert_eq!(result, expected_outputs_clone[i], "Test case {}: [{}]", i, inputs_clone[i].replace('\n', ", "));
                });
            }
        });
    }
}