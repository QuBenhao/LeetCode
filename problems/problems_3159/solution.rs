use serde_json::{json, Value};

pub struct Solution;

impl Solution {
    pub fn occurrences_of_element(nums: Vec<i32>, queries: Vec<i32>, x: i32) -> Vec<i32> {
        
    }
}

#[cfg(feature = "solution_3159")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let nums: Vec<i32> = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	let queries: Vec<i32> = serde_json::from_str(&input_values[1]).expect("Failed to parse input");
	let x: i32 = serde_json::from_str(&input_values[2]).expect("Failed to parse input");
	json!(Solution::occurrences_of_element(nums, queries, x))
}
