#![allow(non_snake_case)]
use serde_json::{json, Value};

pub struct Solution;

impl Solution {
    pub fn print_bin(num: f64) -> String {
        
    }
}

#[cfg(feature = "solution_Interview_05__02")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let num: f64 = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	json!(Solution::print_bin(num))
}
