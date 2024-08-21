use serde_json::{json, Value};

pub struct Solution;

impl Solution {
    pub fn find_min(nums: Vec<i32>) -> i32 {
		let mut left: usize = 0;
		let mut right: usize = nums.len() - 1;
		while left < right {
			if nums[left] < nums[right] {
				return nums[left];
			}
			let mid: usize = left + (right - left) / 2;
			if nums[mid] < nums[right] {
				right = mid;
			} else {
				left = mid + 1;
			}
		}
		nums[left]
    }
}

#[cfg(feature = "solution_153")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let nums: Vec<i32> = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	json!(Solution::find_min(nums))
}
