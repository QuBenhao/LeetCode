use serde_json::{json, Value};

pub struct Solution;

impl Solution {
    pub fn max_target_nodes(edges1: Vec<Vec<i32>>, edges2: Vec<Vec<i32>>, k: i32) -> Vec<i32> {
        
    }
}

#[cfg(feature = "solution_3372")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let edges1: Vec<Vec<i32>> = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	let edges2: Vec<Vec<i32>> = serde_json::from_str(&input_values[1]).expect("Failed to parse input");
	let k: i32 = serde_json::from_str(&input_values[2]).expect("Failed to parse input");
	json!(Solution::max_target_nodes(edges1, edges2, k))
}
