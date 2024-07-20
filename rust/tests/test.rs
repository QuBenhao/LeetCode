const PROBLEM_FOLDER: &str = "problems";
const PROBLEM_ID: &str = "1";

#[cfg(test)]
mod test {
    use std::env;
    use serde_json::Value;
    use crate::{PROBLEM_FOLDER, PROBLEM_ID};

    #[test]
    fn test_solution() {
        let data_file_path = env::current_dir()
            .expect("Failed to get current directory")
            .join(PROBLEM_FOLDER)
            .join(PROBLEM_FOLDER.to_owned() + "_" + PROBLEM_ID)
            .join("testcase");
        if !data_file_path.exists() {
            panic!("TestCase file not found: {:?}", data_file_path);
        }
        let content: String = std::fs::read_to_string(data_file_path)
            .expect("Failed to read data file");
        let mut input_strings: String = String::new();
        let mut expected_outputs: String = String::new();
        content.lines().for_each(|line| {
            if input_strings.is_empty() {
                input_strings = line.to_string();
            } else {
                expected_outputs = line.to_string();
            }
        });
        let inputs: Vec<String> = serde_json::from_str(&input_strings)
            .expect("Unable to parse input strings");
        let expected_outputs: Vec<Value> = serde_json::from_str(&expected_outputs)
            .expect("Unable to parse expected outputs");
        for i in 0..inputs.len() {
            println!("Test case {}: {}", i, inputs[i]);
            let result = solution::solve(inputs[i].to_string());
            assert_eq!(result, expected_outputs[i]);
        }
    }
}