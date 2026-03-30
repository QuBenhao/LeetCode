use serde_json::{json, Value};

pub struct Solution;

impl Solution {
    pub fn generate_string(str1: String, str2: String) -> String {
        
    }
}

#[cfg(feature = "solution_3474")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let str1: String = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	let str2: String = serde_json::from_str(&input_values[1]).expect("Failed to parse input");
	json!(Solution::generate_string(str1, str2))
}
