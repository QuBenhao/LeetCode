use serde_json::{json, Value};

pub struct Solution;

impl Solution {
    pub fn sorted_squares(nums: Vec<i32>) -> Vec<i32> {
		let n = nums.len();
		let mut result: Vec<i32> = vec![0; n];
		let mut left = 0;
		let mut right = n - 1;
		let mut index = n - 1;
		for _ in 0..n {
			if nums[left].abs() > nums[right].abs() {
				result[index] = nums[left] * nums[left];
				left += 1;
			} else {
				result[index] = nums[right] * nums[right];
				right -= 1;
			}
			index = index.wrapping_sub(1);
		}
		result
    }
}

#[cfg(feature = "solution_977")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let nums: Vec<i32> = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	json!(Solution::sorted_squares(nums))
}
