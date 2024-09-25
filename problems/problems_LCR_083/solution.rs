#![allow(non_snake_case)]
use serde_json::{json, Value};

pub struct Solution;

impl Solution {
    pub fn permute(nums: Vec<i32>) -> Vec<Vec<i32>> {
		let mut res = vec![];
		let mut path = vec![];
		fn backtrack(nums: &Vec<i32>, path: &mut Vec<i32>, res: &mut Vec<Vec<i32>>) {
			if path.len() == nums.len() {
				res.push(path.clone());
				return;
			}
			for i in 0..nums.len() {
				if path.contains(&nums[i]) {
					continue;
				}
				path.push(nums[i]);
				backtrack(nums, path, res);
				path.pop();
			}
		}
		backtrack(&nums, &mut path, &mut res);
		res
    }
}

#[cfg(feature = "solution_LCR_083")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let nums: Vec<i32> = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	json!(Solution::permute(nums))
}
