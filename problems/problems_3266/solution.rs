use serde_json::{json, Value};

pub struct Solution;

impl Solution {
    pub fn get_final_state(nums: Vec<i32>, k: i32, multiplier: i32) -> Vec<i32> {
        
    }
}

#[cfg(feature = "solution_3266")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let nums: Vec<i32> = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	let k: i32 = serde_json::from_str(&input_values[1]).expect("Failed to parse input");
	let multiplier: i32 = serde_json::from_str(&input_values[2]).expect("Failed to parse input");
	json!(Solution::get_final_state(nums, k, multiplier))
}
