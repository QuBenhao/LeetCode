use serde_json::{json, Value};

pub struct Solution;

impl Solution {
    pub fn min_operations(mut nums: Vec<i32>) -> i32 {
		let n = nums.len();
		let mut ans = 0;
		for i in 0..n-2 {
			if nums[i] == 0 {
				ans += 1;
				nums[i + 1] ^= 1;
				nums[i + 2] ^= 1;
			}
		}
		if nums[n - 2] == 0 || nums[n - 1] == 0 {
			return -1;
		}
		ans
    }
}

#[cfg(feature = "solution_3191")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let nums: Vec<i32> = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	json!(Solution::min_operations(nums))
}
