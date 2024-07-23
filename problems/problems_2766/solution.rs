use serde_json::{json, Value};

pub struct Solution;

use std::collections::HashSet;

impl Solution {
    pub fn relocate_marbles(nums: Vec<i32>, move_from: Vec<i32>, move_to: Vec<i32>) -> Vec<i32> {
		let mut s: HashSet<i32> = nums.into_iter().collect();
		for i in 0..move_from.len() {
			s.remove(&move_from[i]);
			s.insert(move_to[i]);
		}
		let mut res: Vec<i32> = s.into_iter().collect();
		res.sort();
		res
    }
}

#[cfg(feature = "solution_2766")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let nums: Vec<i32> = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	let move_from: Vec<i32> = serde_json::from_str(&input_values[1]).expect("Failed to parse input");
	let move_to: Vec<i32> = serde_json::from_str(&input_values[2]).expect("Failed to parse input");
	json!(Solution::relocate_marbles(nums, move_from, move_to))
}
