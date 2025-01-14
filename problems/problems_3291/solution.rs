use serde_json::{json, Value};

pub struct Solution;

impl Solution {
    pub fn min_valid_strings(words: Vec<String>, target: String) -> i32 {
        
    }
}

#[cfg(feature = "solution_3291")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let words: Vec<String> = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	let target: String = serde_json::from_str(&input_values[1]).expect("Failed to parse input");
	json!(Solution::min_valid_strings(words, target))
}
