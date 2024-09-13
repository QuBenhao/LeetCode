#![allow(non_snake_case)]
use serde_json::{json, Value};

pub struct Solution;

impl Solution {
    pub fn single_non_duplicate(nums: Vec<i32>) -> i32 {
		let mut left: usize = 0;
		let mut right: usize = nums.len() - 1;
		while left < right {
			let mid = left + (right - left) / 2;
			if nums[mid] == nums[mid ^ 1] {
				left = (mid | 1) + 1;
			} else {
				right = mid;
			}
		}
		nums[left]
    }
}

#[cfg(feature = "solution_LCR_070")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let nums: Vec<i32> = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	json!(Solution::single_non_duplicate(nums))
}
