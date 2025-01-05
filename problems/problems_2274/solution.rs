use serde_json::{json, Value};

pub struct Solution;

impl Solution {
    pub fn max_consecutive(bottom: i32, top: i32, special: Vec<i32>) -> i32 {
        
    }
}

#[cfg(feature = "solution_2274")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let bottom: i32 = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	let top: i32 = serde_json::from_str(&input_values[1]).expect("Failed to parse input");
	let special: Vec<i32> = serde_json::from_str(&input_values[2]).expect("Failed to parse input");
	json!(Solution::max_consecutive(bottom, top, special))
}
