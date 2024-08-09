use serde_json::{json, Value};

pub struct Solution;

impl Solution {
    pub fn word_break(s: String, word_dict: Vec<String>) -> bool {

    }
}

#[cfg(feature = "solution_139")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let s: String = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	let word_dict: Vec<String> = serde_json::from_str(&input_values[1]).expect("Failed to parse input");
	json!(Solution::word_break(s, word_dict))
}
