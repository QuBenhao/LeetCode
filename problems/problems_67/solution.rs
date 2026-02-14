use serde_json::{json, Value};

pub struct Solution;

impl Solution {
    pub fn add_binary(a: String, b: String) -> String {
        
    }
}

#[cfg(feature = "solution_67")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let a: String = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	let b: String = serde_json::from_str(&input_values[1]).expect("Failed to parse input");
	json!(Solution::add_binary(a, b))
}
