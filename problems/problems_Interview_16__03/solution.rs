#![allow(non_snake_case)]
use serde_json::{json, Value};

pub struct Solution;

impl Solution {
    pub fn intersection(start1: Vec<i32>, end1: Vec<i32>, start2: Vec<i32>, end2: Vec<i32>) -> Vec<f64> {
        
    }
}

#[cfg(feature = "solution_Interview_16__03")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let start1: Vec<i32> = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	let end1: Vec<i32> = serde_json::from_str(&input_values[1]).expect("Failed to parse input");
	let start2: Vec<i32> = serde_json::from_str(&input_values[2]).expect("Failed to parse input");
	let end2: Vec<i32> = serde_json::from_str(&input_values[3]).expect("Failed to parse input");
	json!(Solution::intersection(start1, end1, start2, end2))
}
