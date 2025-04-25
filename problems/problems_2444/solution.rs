use serde_json::{json, Value};

pub struct Solution;

impl Solution {
    pub fn count_subarrays(nums: Vec<i32>, min_k: i32, max_k: i32) -> i64 {
        
    }
}

#[cfg(feature = "solution_2444")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let nums: Vec<i32> = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	let min_k: i32 = serde_json::from_str(&input_values[1]).expect("Failed to parse input");
	let max_k: i32 = serde_json::from_str(&input_values[2]).expect("Failed to parse input");
	json!(Solution::count_subarrays(nums, min_k, max_k))
}
