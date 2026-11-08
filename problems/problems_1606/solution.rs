use serde_json::{json, Value};

pub struct Solution;

impl Solution {
    pub fn busiest_servers(k: i32, arrival: Vec<i32>, load: Vec<i32>) -> Vec<i32> {
        
    }
}

#[cfg(feature = "solution_1606")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let k: i32 = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	let arrival: Vec<i32> = serde_json::from_str(&input_values[1]).expect("Failed to parse input");
	let load: Vec<i32> = serde_json::from_str(&input_values[2]).expect("Failed to parse input");
	json!(Solution::busiest_servers(k, arrival, load))
}
