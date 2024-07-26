use serde_json::{json, Value};

pub struct Solution;

impl Solution {
    pub fn search_range(nums: Vec<i32>, target: i32) -> Vec<i32> {
		let bisect_left = |nums: &Vec<i32>, target: &i32| -> i32 {
			let mut left = 0;
			let mut right = nums.len() as i32;
			while left < right {
				let mid = left + (right - left) / 2;
				if nums[mid as usize] < *target {
					left = mid + 1;
				} else {
					right = mid;
				}
			}
			left
		};
		let bisect_right = |nums: &Vec<i32>, target: &i32| -> i32 {
			let mut left = 0;
			let mut right = nums.len() as i32;
			while left < right {
				let mid = left + (right - left) / 2;
				if nums[mid as usize] <= *target {
					left = mid + 1;
				} else {
					right = mid;
				}
			}
			left
		};
		let left = bisect_left(&nums, &target);
		let right = bisect_right(&nums, &target) - 1;
		if left <= right && nums[left as usize] == target {
			vec![left, right]
		} else {
			vec![-1, -1]
		}
	}
}

#[cfg(feature = "solution_34")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let nums: Vec<i32> = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	let target: i32 = serde_json::from_str(&input_values[1]).expect("Failed to parse input");
	json!(Solution::search_range(nums, target))
}
