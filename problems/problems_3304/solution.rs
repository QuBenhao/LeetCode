use serde_json::{json, Value};

pub struct Solution;

impl Solution {
    pub fn kth_character(k: i32) -> char {
        
    }
}

#[cfg(feature = "solution_3304")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let k: i32 = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	json!(Solution::kth_character(k))
}
