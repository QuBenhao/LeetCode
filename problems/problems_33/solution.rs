use serde_json::{json, Value};

pub struct Solution;

impl Solution {
    pub fn search(nums: Vec<i32>, target: i32) -> i32 {
		let mut left: usize = 0;
		let mut right: usize = nums.len() - 1;
		while left < right {
			let mid = left + (right - left) / 2;
			if nums[mid] >= nums[0] {
				left = mid + 1;
			} else {
				right = mid;
			}
		}
		if target >= nums[0] {
			left = 0;
		} else {
			right = nums.len() - 1;
		}
		while left < right {
			let mid = left + (right - left) / 2;
			if nums[mid] < target {
				left = mid + 1;
			} else {
				right = mid;
			}
		}
		if left < nums.len() && nums[left] == target {
			left as i32
		} else {
			-1
		}
    }
}

#[cfg(feature = "solution_33")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let nums: Vec<i32> = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	let target: i32 = serde_json::from_str(&input_values[1]).expect("Failed to parse input");
	json!(Solution::search(nums, target))
}
