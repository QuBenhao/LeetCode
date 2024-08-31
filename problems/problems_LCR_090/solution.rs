#![allow(non_snake_case)]
use serde_json::{json, Value};

pub struct Solution;

impl Solution {
    pub fn rob(nums: Vec<i32>) -> i32 {
		let n = nums.len();
		let mut dp_rob = nums[0];
		let mut dp_not_rob = nums[0];
		for i in 2..n.checked_sub(1).unwrap_or(1) {
			let temp = dp_rob;
			dp_rob = dp_not_rob + nums[i];
			dp_not_rob = dp_not_rob.max(temp);
		}
		let res = dp_not_rob.max(dp_rob);
		dp_rob = 0;
		dp_not_rob = 0;
		for i in 1..n {
			let temp = dp_rob;
			dp_rob = dp_not_rob + nums[i];
			dp_not_rob = dp_not_rob.max(temp);
		}
		res.max(dp_not_rob.max(dp_rob))
    }
}

#[cfg(feature = "solution_LCR_090")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let nums: Vec<i32> = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	json!(Solution::rob(nums))
}
