use serde_json::{json, Value};

pub struct Solution;

impl Solution {
    pub fn compare_version(version1: String, version2: String) -> i32 {
        
    }
}

#[cfg(feature = "solution_165")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let version1: String = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	let version2: String = serde_json::from_str(&input_values[1]).expect("Failed to parse input");
	json!(Solution::compare_version(version1, version2))
}
