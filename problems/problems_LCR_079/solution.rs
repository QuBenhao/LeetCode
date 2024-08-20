#![allow(non_snake_case)]
use serde_json::{json, Value};

pub struct Solution;

impl Solution {
    pub fn subsets(nums: Vec<i32>) -> Vec<Vec<i32>> {
		let mut ans: Vec<Vec<i32>> = Vec::new();
		let mut path: Vec<i32> = Vec::new();
		Self::dfs(&nums, 0, &mut path, &mut ans);
		ans
    }

	fn dfs(nums: &Vec<i32>, start: usize, path: &mut Vec<i32>, ans: &mut Vec<Vec<i32>>) {
		if start == nums.len() {
			ans.push(path.clone());
			return;
		}
		Self::dfs(nums, start + 1, path, ans);
		path.push(nums[start]);
		Self::dfs(nums, start + 1, path, ans);
		path.pop();
	}
}

#[cfg(feature = "solution_LCR_079")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let nums: Vec<i32> = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	json!(Solution::subsets(nums))
}
