use serde_json::{json, Value};

pub struct Solution;

impl Solution {
    pub fn smallest_equivalent_string(s1: String, s2: String, base_str: String) -> String {
        
    }
}

#[cfg(feature = "solution_1061")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let s1: String = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	let s2: String = serde_json::from_str(&input_values[1]).expect("Failed to parse input");
	let base_str: String = serde_json::from_str(&input_values[2]).expect("Failed to parse input");
	json!(Solution::smallest_equivalent_string(s1, s2, base_str))
}
