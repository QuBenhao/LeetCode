use serde_json::{json, Value};

pub struct Solution;

impl Solution {
    pub fn maximum_value_sum(nums: Vec<i32>, k: i32, edges: Vec<Vec<i32>>) -> i64 {
        
    }
}

#[cfg(feature = "solution_3068")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let nums: Vec<i32> = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	let k: i32 = serde_json::from_str(&input_values[1]).expect("Failed to parse input");
	let edges: Vec<Vec<i32>> = serde_json::from_str(&input_values[2]).expect("Failed to parse input");
	json!(Solution::maximum_value_sum(nums, k, edges))
}
