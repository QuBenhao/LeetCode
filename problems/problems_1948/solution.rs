use serde_json::{json, Value};

pub struct Solution;

impl Solution {
    pub fn delete_duplicate_folder(paths: Vec<Vec<String>>) -> Vec<Vec<String>> {
        
    }
}

#[cfg(feature = "solution_1948")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let paths: Vec<Vec<String>> = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	json!(Solution::delete_duplicate_folder(paths))
}
