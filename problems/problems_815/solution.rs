use serde_json::{json, Value};

pub struct Solution;

impl Solution {
    pub fn num_buses_to_destination(routes: Vec<Vec<i32>>, source: i32, target: i32) -> i32 {

    }
}

#[cfg(feature = "solution_815")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let routes: Vec<Vec<i32>> = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	let source: i32 = serde_json::from_str(&input_values[1]).expect("Failed to parse input");
	let target: i32 = serde_json::from_str(&input_values[2]).expect("Failed to parse input");
	json!(Solution::num_buses_to_destination(routes, source, target))
}
