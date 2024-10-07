#![allow(non_snake_case)]
use serde_json::{json, Value};

pub struct Solution;

impl Solution {
		fn dfs(graph: &Vec<Vec<i32>>, node: i32, path: &mut Vec<i32>, res: &mut Vec<Vec<i32>>) {
				if node == graph.len() as i32 - 1 {
						res.push(path.clone());
						return;
				}
				for &next in &graph[node as usize] {
						path.push(next);
						Self::dfs(graph, next, path, res);
						path.pop();
				}
		}
    pub fn all_paths_source_target(graph: Vec<Vec<i32>>) -> Vec<Vec<i32>> {
				let mut res = vec![];
				let mut path = vec![0];
				Self::dfs(&graph, 0, &mut path, &mut res);
				res
    }
}

#[cfg(feature = "solution_LCR_110")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let graph: Vec<Vec<i32>> = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	json!(Solution::all_paths_source_target(graph))
}
