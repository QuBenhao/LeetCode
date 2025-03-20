use serde_json::{json, Value};

pub struct Solution;

impl Solution {
    pub fn maximum_or(nums: Vec<i32>, k: i32) -> i64 {
        
    }
}

#[cfg(feature = "solution_2680")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let nums: Vec<i32> = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	let k: i32 = serde_json::from_str(&input_values[1]).expect("Failed to parse input");
	json!(Solution::maximum_or(nums, k))
}
