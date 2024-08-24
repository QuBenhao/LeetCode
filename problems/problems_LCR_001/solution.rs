#![allow(non_snake_case)]
use serde_json::{json, Value};

pub struct Solution;

impl Solution {
    pub fn divide(a: i32, b: i32) -> i32 {

    }
}

#[cfg(feature = "solution_LCR_001")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let a: i32 = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	let b: i32 = serde_json::from_str(&input_values[1]).expect("Failed to parse input");
	json!(Solution::divide(a, b))
}
