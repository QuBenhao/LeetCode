use serde_json::{json, Value};

pub struct Solution;
use std::cmp::{max, min};
impl Solution {
    pub fn smallest_range_i(nums: Vec<i32>, k: i32) -> i32 {
		let mut min_val = nums[0];
		let mut max_val = nums[0];
		for i in 1..nums.len() {
			min_val = min(min_val, nums[i]);
			max_val = max(max_val, nums[i]);
		}
		max(0, max_val - min_val - 2 * k)
    }
}

#[cfg(feature = "solution_908")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let nums: Vec<i32> = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	let k: i32 = serde_json::from_str(&input_values[1]).expect("Failed to parse input");
	json!(Solution::smallest_range_i(nums, k))
}
