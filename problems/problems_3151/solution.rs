use serde_json::{json, Value};

pub struct Solution;

impl Solution {
    pub fn is_array_special(nums: Vec<i32>) -> bool {
		let mut last: i32 = (nums[0] & 1) ^ 1;
		for num in nums {
			if num & 1 == last {
				return false;
			}
			last ^= 1;
		}
		true
    }
}

#[cfg(feature = "solution_3151")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let nums: Vec<i32> = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	json!(Solution::is_array_special(nums))
}
