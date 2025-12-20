#![allow(non_snake_case)]
use serde_json::{json, Value};

pub struct Solution;

impl Solution {
    pub fn merge(a: &mut Vec<i32>, m: i32, b: &mut Vec<i32>, n: i32) {
        
    }
}

#[cfg(feature = "solution_Interview_10__01")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let mut a: Vec<i32> = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	let m: i32 = serde_json::from_str(&input_values[1]).expect("Failed to parse input");
	let mut b: Vec<i32> = serde_json::from_str(&input_values[2]).expect("Failed to parse input");
	let n: i32 = serde_json::from_str(&input_values[3]).expect("Failed to parse input");
	Solution::merge(&mut a, m, &mut b, n);
	json!(a)
}
