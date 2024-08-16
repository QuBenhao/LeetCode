#![allow(non_snake_case)]
use serde_json::{json, Value};

pub struct Solution;

impl Solution {
    pub fn check_inclusion(s1: String, s2: String) -> bool {

    }
}

#[cfg(feature = "solution_LCR_014")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let s1: String = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	let s2: String = serde_json::from_str(&input_values[1]).expect("Failed to parse input");
	json!(Solution::check_inclusion(s1, s2))
}
