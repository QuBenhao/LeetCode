use serde_json::{json, Value};

pub struct Solution;

impl Solution {
    pub fn distance_between_bus_stops(distance: Vec<i32>, start: i32, destination: i32) -> i32 {

    }
}

#[cfg(feature = "solution_1184")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let distance: Vec<i32> = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	let start: i32 = serde_json::from_str(&input_values[1]).expect("Failed to parse input");
	let destination: i32 = serde_json::from_str(&input_values[2]).expect("Failed to parse input");
	json!(Solution::distance_between_bus_stops(distance, start, destination))
}
