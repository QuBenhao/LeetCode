#![allow(non_snake_case)]
use serde_json::{json, Value};

pub struct Solution;

impl Solution {
    pub fn count_bits(n: i32) -> Vec<i32> {
		let mut res = vec![0; (n + 1) as usize];
		for i in 1..=n as usize {
			res[i] = res[i >> 1] + (i & 1) as i32;
		}
		res
    }
}

#[cfg(feature = "solution_LCR_003")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let n: i32 = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	json!(Solution::count_bits(n))
}
