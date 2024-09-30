use serde_json::{json, Value};

pub struct Solution;

impl Solution {
    pub fn mincost_tickets(days: Vec<i32>, costs: Vec<i32>) -> i32 {

    }
}

#[cfg(feature = "solution_983")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let days: Vec<i32> = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	let costs: Vec<i32> = serde_json::from_str(&input_values[1]).expect("Failed to parse input");
	json!(Solution::mincost_tickets(days, costs))
}
