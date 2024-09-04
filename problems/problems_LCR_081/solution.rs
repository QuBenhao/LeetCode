#![allow(non_snake_case)]
use serde_json::{json, Value};

pub struct Solution;

impl Solution {
    pub fn combination_sum(candidates: Vec<i32>, target: i32) -> Vec<Vec<i32>> {
		let mut candidates = candidates;
		candidates.sort_unstable();
		let mut ans = vec![];
		let mut path = vec![];
		fn backtrack(candidates: &Vec<i32>, target: i32, path: &mut Vec<i32>, ans: &mut Vec<Vec<i32>>, start: usize) {
			if target == 0 {
				ans.push(path.clone());
				return;
			}
			for i in start..candidates.len() {
				if target < candidates[i] {
					break;
				}
				path.push(candidates[i]);
				backtrack(candidates, target - candidates[i], path, ans, i);
				path.pop();
			}
		}
		backtrack(&candidates, target, &mut path, &mut ans, 0);
		ans
    }
}

#[cfg(feature = "solution_LCR_081")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let candidates: Vec<i32> = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	let target: i32 = serde_json::from_str(&input_values[1]).expect("Failed to parse input");
	json!(Solution::combination_sum(candidates, target))
}
