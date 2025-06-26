use serde_json::{json, Value};

pub struct Solution;

impl Solution {
    pub fn longest_subsequence_repeated_k(s: String, k: i32) -> String {
        
    }
}

#[cfg(feature = "solution_2014")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let s: String = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	let k: i32 = serde_json::from_str(&input_values[1]).expect("Failed to parse input");
	json!(Solution::longest_subsequence_repeated_k(s, k))
}
