#![allow(non_snake_case)]
use serde_json::{json, Value};

pub struct Solution;

impl Solution {
    pub fn three_sum(nums: Vec<i32>) -> Vec<Vec<i32>> {
		let mut ans: Vec<Vec<i32>> = vec![];
		let mut nums = nums;
		nums.sort_unstable();
		let n = nums.len();
		for i in 0..n.checked_sub(2).unwrap_or(0) {
			if i > 0 && nums[i] == nums[i-1] {
				continue;
			}
			let mut j = i + 1;
			let mut k = n - 1;
			while j < k {
				let sum = nums[i] + nums[j] + nums[k];
				if sum == 0 {
					ans.push(vec![nums[i], nums[j], nums[k]]);
					j += 1;
					k -= 1;
					while j < k && nums[j] == nums[j-1] {
						j += 1;
					}
					while j < k && nums[k] == nums[k+1] {
						k -= 1;
					}
				} else if sum < 0 {
					j += 1;
				} else {
					k -= 1;
				}
			}
		}
		ans
    }
}

#[cfg(feature = "solution_LCR_007")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let nums: Vec<i32> = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	json!(Solution::three_sum(nums))
}
