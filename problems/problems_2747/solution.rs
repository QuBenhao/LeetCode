use serde_json::{json, Value};

pub struct Solution;

impl Solution {
    pub fn count_servers(n: i32, logs: Vec<Vec<i32>>, x: i32, queries: Vec<i32>) -> Vec<i32> {
        
    }
}

#[cfg(feature = "solution_2747")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let n: i32 = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	let logs: Vec<Vec<i32>> = serde_json::from_str(&input_values[1]).expect("Failed to parse input");
	let x: i32 = serde_json::from_str(&input_values[2]).expect("Failed to parse input");
	let queries: Vec<i32> = serde_json::from_str(&input_values[3]).expect("Failed to parse input");
	json!(Solution::count_servers(n, logs, x, queries))
}
