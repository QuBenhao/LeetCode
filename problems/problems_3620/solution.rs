use serde_json::{json, Value};

pub struct Solution;

impl Solution {
    pub fn find_max_path_score(edges: Vec<Vec<i32>>, online: Vec<bool>, k: i64) -> i32 {
        
    }
}

#[cfg(feature = "solution_3620")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let edges: Vec<Vec<i32>> = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	let online: Vec<bool> = serde_json::from_str(&input_values[1]).expect("Failed to parse input");
	let k: i64 = serde_json::from_str(&input_values[2]).expect("Failed to parse input");
	json!(Solution::find_max_path_score(edges, online, k))
}
