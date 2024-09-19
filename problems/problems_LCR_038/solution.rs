#![allow(non_snake_case)]
use serde_json::{json, Value};

pub struct Solution;

impl Solution {
    pub fn daily_temperatures(temperatures: Vec<i32>) -> Vec<i32> {
		let n = temperatures.len();
		let mut ans = vec![0; n];
		let mut stack = Vec::new();
		for i in 0..n {
			while !stack.is_empty() && temperatures[i] > temperatures[*stack.last().unwrap()] {
				let j = stack.pop().unwrap();
				ans[j] = (i - j) as i32;
			}
			stack.push(i);
		}
		ans
    }
}

#[cfg(feature = "solution_LCR_038")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let temperatures: Vec<i32> = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	json!(Solution::daily_temperatures(temperatures))
}
