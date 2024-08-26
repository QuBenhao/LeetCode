#![allow(non_snake_case)]
use serde_json::{json, Value};

pub struct Solution;

impl Solution {
    pub fn search_insert(nums: Vec<i32>, target: i32) -> i32 {
		let mut left: usize = 0;
		let mut right: usize = nums.len();
		while left < right {
			let mid = left + (right - left) / 2;
			if nums[mid] < target {
				left = mid + 1;
			} else {
				right = mid;
			}
		}
		left as i32
    }
}

#[cfg(feature = "solution_LCR_068")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let nums: Vec<i32> = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	let target: i32 = serde_json::from_str(&input_values[1]).expect("Failed to parse input");
	json!(Solution::search_insert(nums, target))
}
