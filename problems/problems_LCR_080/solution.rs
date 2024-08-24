#![allow(non_snake_case)]
use serde_json::{json, Value};

pub struct Solution;

impl Solution {
    pub fn combine(n: i32, k: i32) -> Vec<Vec<i32>> {
		let mut ans: Vec<Vec<i32>> = vec![];
		let mut path: Vec<i32> = vec![];
		Solution::backtrack(n, k, 1, &mut path, &mut ans);
		ans
    }

	fn backtrack(n: i32, k: i32, start: i32, path: &mut Vec<i32>, ans: &mut Vec<Vec<i32>>) {
		if path.len() == k as usize {
			ans.push(path.clone());
			return;
		}
		for i in start..=n {
			path.push(i);
			Solution::backtrack(n, k, i + 1, path, ans);
			path.pop();
		}
	}
}

#[cfg(feature = "solution_LCR_080")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let n: i32 = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	let k: i32 = serde_json::from_str(&input_values[1]).expect("Failed to parse input");
	json!(Solution::combine(n, k))
}
