use serde_json::{json, Value};

pub struct Solution;

impl Solution {
    pub fn min_number_of_seconds(mountain_height: i32, worker_times: Vec<i32>) -> i64 {
        
    }
}

#[cfg(feature = "solution_3296")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let mountain_height: i32 = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	let worker_times: Vec<i32> = serde_json::from_str(&input_values[1]).expect("Failed to parse input");
	json!(Solution::min_number_of_seconds(mountain_height, worker_times))
}
