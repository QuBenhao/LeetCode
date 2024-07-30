use serde_json::{json, Value};

pub struct Solution;

impl Solution {
	fn dfs(candidates: &Vec<i32>, target: i32, index: usize, path: &mut Vec<i32>, ans: &mut Vec<Vec<i32>>) {
		if target == 0 {
			ans.push(path.clone());
			return;
		}
		if index == candidates.len() {
			return;
		}
		if candidates[index] > target {
			return;
		}
		path.push(candidates[index]);
		Solution::dfs(candidates, target - candidates[index], index, path, ans);
		path.pop();
		Solution::dfs(candidates, target, index + 1, path, ans);
	}
    pub fn combination_sum(candidates: Vec<i32>, target: i32) -> Vec<Vec<i32>> {
		let mut ans: Vec<Vec<i32>> = Vec::new();
		let mut path: Vec<i32> = Vec::new();
		let mut candidates: Vec<i32> = candidates;
		candidates.sort();
		Solution::dfs(&candidates, target, 0, &mut path, &mut ans);
		ans
    }
}

#[cfg(feature = "solution_39")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let candidates: Vec<i32> = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	let target: i32 = serde_json::from_str(&input_values[1]).expect("Failed to parse input");
	json!(Solution::combination_sum(candidates, target))
}
