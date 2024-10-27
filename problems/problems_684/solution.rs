use serde_json::{json, Value};

pub struct Solution;

impl Solution {
	fn find(parent: &mut Vec<i32>, u: i32) -> i32 {
		if parent[u as usize] != u {
			parent[u as usize] = Solution::find(parent, parent[u as usize]);
		}
		parent[u as usize]
	}

	fn union(parent: &mut Vec<i32>, u: i32, v: i32) {
		let pu = Solution::find(parent, u);
		let pv = Solution::find(parent, v);
		if pu != pv {
			parent[pu as usize] = pv;
		}
	}

    pub fn find_redundant_connection(edges: Vec<Vec<i32>>) -> Vec<i32> {
		let mut parent = vec![0; edges.len() + 1];
		for i in 0..parent.len() {
			parent[i] = i as i32;
		}
		for edge in edges {
			let u = edge[0];
			let v = edge[1];
			if Solution::find(&mut parent, u) == Solution::find(&mut parent, v) {
				return vec![u, v];
			}
			Solution::union(&mut parent, u, v);
		}
		vec![]
    }
}

#[cfg(feature = "solution_684")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let edges: Vec<Vec<i32>> = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	json!(Solution::find_redundant_connection(edges))
}
