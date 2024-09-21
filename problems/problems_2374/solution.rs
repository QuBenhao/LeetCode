use serde_json::{json, Value};

pub struct Solution;

impl Solution {
    pub fn edge_score(edges: Vec<i32>) -> i32 {
		let mut ans: i32 = 0;
		let n = edges.len();
		let mut counter: Vec<i64> = vec![0; n];
		for i in 0..n {
			counter[edges[i] as usize] += i as i64;
			if counter[edges[i] as usize] > counter[ans as usize] {
				ans = edges[i];
			} else if counter[edges[i] as usize] == counter[ans as usize] {
				ans = ans.min(edges[i]);
			}
		}
		ans
    }
}

#[cfg(feature = "solution_2374")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let edges: Vec<i32> = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	json!(Solution::edge_score(edges))
}
