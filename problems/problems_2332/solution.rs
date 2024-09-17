use serde_json::{json, Value};

pub struct Solution;

impl Solution {
    pub fn latest_time_catch_the_bus(buses: Vec<i32>, passengers: Vec<i32>, capacity: i32) -> i32 {

    }
}

#[cfg(feature = "solution_2332")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let buses: Vec<i32> = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	let passengers: Vec<i32> = serde_json::from_str(&input_values[1]).expect("Failed to parse input");
	let capacity: i32 = serde_json::from_str(&input_values[2]).expect("Failed to parse input");
	json!(Solution::latest_time_catch_the_bus(buses, passengers, capacity))
}
