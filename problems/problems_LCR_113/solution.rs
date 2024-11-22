#![allow(non_snake_case)]
use serde_json::{json, Value};

pub struct Solution;

impl Solution {
    pub fn find_order(num_courses: i32, prerequisites: Vec<Vec<i32>>) -> Vec<i32> {

    }
}

#[cfg(feature = "solution_LCR_113")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let num_courses: i32 = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	let prerequisites: Vec<Vec<i32>> = serde_json::from_str(&input_values[1]).expect("Failed to parse input");
	json!(Solution::find_order(num_courses, prerequisites))
}
