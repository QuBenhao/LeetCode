#![allow(non_snake_case)]
use serde_json::{json, Value};

pub struct Solution;

impl Solution {
    pub fn open_lock(deadends: Vec<String>, target: String) -> i32 {

    }
}

#[cfg(feature = "solution_LCR_109")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let deadends: Vec<String> = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	let target: String = serde_json::from_str(&input_values[1]).expect("Failed to parse input");
	json!(Solution::open_lock(deadends, target))
}
