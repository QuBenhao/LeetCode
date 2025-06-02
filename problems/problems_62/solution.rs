use serde_json::{json, Value};

pub struct Solution;

impl Solution {
    pub fn unique_paths(m: i32, n: i32) -> i32 {
        
    }
}

#[cfg(feature = "solution_62")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let m: i32 = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	let n: i32 = serde_json::from_str(&input_values[1]).expect("Failed to parse input");
	json!(Solution::unique_paths(m, n))
}
