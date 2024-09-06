#![allow(non_snake_case)]
use serde_json::{json, Value};

pub struct Solution;

impl Solution {
    pub fn is_bipartite(graph: Vec<Vec<i32>>) -> bool {
		let n = graph.len();
		let mut color: Vec<i32> = vec![-1; n];
		fn dfs(graph: &Vec<Vec<i32>>, color: &mut Vec<i32>, node: usize, c: i32) -> bool {
			if color[node] != -1 {
				return color[node] == c;
			}
			color[node] = c;
			let nxt = 1 ^ c;
			for other in &graph[node] {
				let other = *other as usize;
				if !dfs(graph, color, other, nxt) {
					return false;
				}
			}
			true
		}
		for i in 0..n {
			if color[i] != -1 {
				continue;
			}
			if !dfs(&graph, &mut color, i, 0) {
				return false;
			}
		}
		true
    }
}

#[cfg(feature = "solution_LCR_106")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let graph: Vec<Vec<i32>> = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	json!(Solution::is_bipartite(graph))
}
