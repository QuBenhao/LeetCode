use serde_json::{json, Value};

pub struct Solution;

impl Solution {
    pub fn minimum_time(time: Vec<i32>, total_trips: i32) -> i64 {

    }
}

#[cfg(feature = "solution_2187")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let time: Vec<i32> = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	let total_trips: i32 = serde_json::from_str(&input_values[1]).expect("Failed to parse input");
	json!(Solution::minimum_time(time, total_trips))
}
