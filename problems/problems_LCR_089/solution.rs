#![allow(non_snake_case)]
use serde_json::{json, Value};

pub struct Solution;

impl Solution {
    pub fn rob(nums: Vec<i32>) -> i32 {
		let mut dp_not_rob = 0;
		let mut dp_rob = 0;
		for num in nums {
			let temp = dp_not_rob;
			dp_not_rob = dp_not_rob.max(dp_rob);
			dp_rob = temp + num;
		}
		dp_rob.max(dp_not_rob)
    }
}

#[cfg(feature = "solution_LCR_089")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let nums: Vec<i32> = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	json!(Solution::rob(nums))
}
