use serde_json::{json, Value};

pub struct Solution;

impl Solution {
    pub fn shortest_path(n: i32, edges: Vec<Vec<i32>>, labels: String, k: i32) -> i32 {
        
    }
}

#[cfg(feature = "solution_3970")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let n: i32 = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	let edges: Vec<Vec<i32>> = serde_json::from_str(&input_values[1]).expect("Failed to parse input");
	let labels: String = serde_json::from_str(&input_values[2]).expect("Failed to parse input");
	let k: i32 = serde_json::from_str(&input_values[3]).expect("Failed to parse input");
	json!(Solution::shortest_path(n, edges, labels, k))
}
