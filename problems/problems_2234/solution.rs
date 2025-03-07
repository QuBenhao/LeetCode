use serde_json::{json, Value};

pub struct Solution;

impl Solution {
    pub fn maximum_beauty(flowers: Vec<i32>, new_flowers: i64, target: i32, full: i32, partial: i32) -> i64 {
        
    }
}

#[cfg(feature = "solution_2234")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let flowers: Vec<i32> = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	let new_flowers: i64 = serde_json::from_str(&input_values[1]).expect("Failed to parse input");
	let target: i32 = serde_json::from_str(&input_values[2]).expect("Failed to parse input");
	let full: i32 = serde_json::from_str(&input_values[3]).expect("Failed to parse input");
	let partial: i32 = serde_json::from_str(&input_values[4]).expect("Failed to parse input");
	json!(Solution::maximum_beauty(flowers, new_flowers, target, full, partial))
}
