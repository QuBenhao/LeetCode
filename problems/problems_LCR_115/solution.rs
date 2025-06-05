#![allow(non_snake_case)]
use serde_json::{json, Value};

pub struct Solution;

impl Solution {
    pub fn sequence_reconstruction(nums: Vec<i32>, sequences: Vec<Vec<i32>>) -> bool {

    }
}

#[cfg(feature = "solution_LCR_115")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let nums: Vec<i32> = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	let sequences: Vec<Vec<i32>> = serde_json::from_str(&input_values[1]).expect("Failed to parse input");
	json!(Solution::sequence_reconstruction(nums, sequences))
}
