use serde_json::{json, Value};

pub struct Solution;

impl Solution {
    pub fn kth_character(k: i64, operations: Vec<i32>) -> char {
        
    }
}

#[cfg(feature = "solution_3307")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let k: i64 = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	let operations: Vec<i32> = serde_json::from_str(&input_values[1]).expect("Failed to parse input");
	json!(Solution::kth_character(k, operations))
}
