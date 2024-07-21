use std::env;
use serde_json::Value;

pub fn load_test_cases(problem_folder: &str, problem_id: &str) -> (Vec<String>, Vec<Value>) {
    let data_file_path = env::current_dir()
        .expect("Failed to get current directory")
        .join(problem_folder)
        .join(problem_folder.to_owned() + "_" + problem_id)
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
    (inputs, expected_outputs)
}