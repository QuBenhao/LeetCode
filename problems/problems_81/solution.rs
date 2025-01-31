use serde_json::{json, Value};

pub struct Solution;

impl Solution {
    pub fn search(nums: Vec<i32>, target: i32) -> bool {
        
    }
}

#[cfg(feature = "solution_81")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let nums: Vec<i32> = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	let target: i32 = serde_json::from_str(&input_values[1]).expect("Failed to parse input");
	json!(Solution::search(nums, target))
}
