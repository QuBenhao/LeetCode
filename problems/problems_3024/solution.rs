use serde_json::{json, Value};

pub struct Solution;

impl Solution {
    pub fn triangle_type(nums: Vec<i32>) -> String {
        
    }
}

#[cfg(feature = "solution_3024")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let nums: Vec<i32> = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	json!(Solution::triangle_type(nums))
}
