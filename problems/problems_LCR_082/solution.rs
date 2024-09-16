#![allow(non_snake_case)]
use serde_json::{json, Value};

pub struct Solution;

impl Solution {
    pub fn combination_sum2(candidates: Vec<i32>, target: i32) -> Vec<Vec<i32>> {
		let mut result = Vec::new();
		let mut path = Vec::new();
		let mut candidates = candidates;
		candidates.sort_unstable();
		fn backtrack(candidates: &Vec<i32>, target: i32, start: usize, path: &mut Vec<i32>, result: &mut Vec<Vec<i32>>) {
			if target == 0 {
				result.push(path.clone());
				return;
			}
			for i in start..candidates.len() {
				if i > start && candidates[i] == candidates[i - 1] {
					continue;
				}
				if target < candidates[i] {
					break;
				}
				path.push(candidates[i]);
				backtrack(candidates, target - candidates[i], i + 1, path, result);
				path.pop();
			}
		}
		backtrack(&candidates, target, 0, &mut path, &mut result);
		result
    }
}

#[cfg(feature = "solution_LCR_082")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let candidates: Vec<i32> = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	let target: i32 = serde_json::from_str(&input_values[1]).expect("Failed to parse input");
	json!(Solution::combination_sum2(candidates, target))
}
