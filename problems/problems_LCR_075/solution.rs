#![allow(non_snake_case)]
use serde_json::{json, Value};

pub struct Solution;

impl Solution {
    pub fn relative_sort_array(arr1: Vec<i32>, arr2: Vec<i32>) -> Vec<i32> {

    }
}

#[cfg(feature = "solution_LCR_075")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let arr1: Vec<i32> = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	let arr2: Vec<i32> = serde_json::from_str(&input_values[1]).expect("Failed to parse input");
	json!(Solution::relative_sort_array(arr1, arr2))
}
