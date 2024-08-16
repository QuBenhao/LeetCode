use serde_json::{json, Value};

pub struct Solution;

impl Solution {
    pub fn longest_common_subsequence(text1: String, text2: String) -> i32 {

    }
}

#[cfg(feature = "solution_1143")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let text1: String = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	let text2: String = serde_json::from_str(&input_values[1]).expect("Failed to parse input");
	json!(Solution::longest_common_subsequence(text1, text2))
}
