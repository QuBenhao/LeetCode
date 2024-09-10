#![allow(non_snake_case)]
use serde_json::{json, Value};

pub struct Solution;

impl Solution {
    pub fn is_anagram(s: String, t: String) -> bool {

    }
}

#[cfg(feature = "solution_LCR_032")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let s: String = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	let t: String = serde_json::from_str(&input_values[1]).expect("Failed to parse input");
	json!(Solution::is_anagram(s, t))
}
