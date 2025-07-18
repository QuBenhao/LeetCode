use serde_json::{json, Value};

pub struct Solution;

impl Solution {
    pub fn remove_subfolders(folder: Vec<String>) -> Vec<String> {
        
    }
}

#[cfg(feature = "solution_1233")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let folder: Vec<String> = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	json!(Solution::remove_subfolders(folder))
}
