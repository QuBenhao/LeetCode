#![allow(non_snake_case)]
use serde_json::{json, Value};

pub struct Solution;

impl Solution {
    pub fn find_min_difference(time_points: Vec<String>) -> i32 {

    }
}

#[cfg(feature = "solution_LCR_035")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let time_points: Vec<String> = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	json!(Solution::find_min_difference(time_points))
}
