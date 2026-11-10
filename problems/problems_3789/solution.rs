use serde_json::{json, Value};

pub struct Solution;

impl Solution {
    pub fn minimum_cost(cost1: i32, cost2: i32, cost_both: i32, need1: i32, need2: i32) -> i64 {
        
    }
}

#[cfg(feature = "solution_3789")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let cost1: i32 = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	let cost2: i32 = serde_json::from_str(&input_values[1]).expect("Failed to parse input");
	let cost_both: i32 = serde_json::from_str(&input_values[2]).expect("Failed to parse input");
	let need1: i32 = serde_json::from_str(&input_values[3]).expect("Failed to parse input");
	let need2: i32 = serde_json::from_str(&input_values[4]).expect("Failed to parse input");
	json!(Solution::minimum_cost(cost1, cost2, cost_both, need1, need2))
}
