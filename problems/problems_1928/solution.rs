use serde_json::{json, Value};

pub struct Solution;

impl Solution {
    pub fn min_cost(max_time: i32, edges: Vec<Vec<i32>>, passing_fees: Vec<i32>) -> i32 {

    }
}

#[cfg(feature = "solution_1928")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let max_time: i32 = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	let edges: Vec<Vec<i32>> = serde_json::from_str(&input_values[1]).expect("Failed to parse input");
	let passing_fees: Vec<i32> = serde_json::from_str(&input_values[2]).expect("Failed to parse input");
	json!(Solution::min_cost(max_time, edges, passing_fees))
}
