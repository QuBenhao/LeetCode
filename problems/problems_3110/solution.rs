use serde_json::{json, Value};

pub struct Solution;

impl Solution {
    pub fn score_of_string(s: String) -> i32 {
        
    }
}

#[cfg(feature = "solution_3110")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let s: String = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	json!(Solution::score_of_string(s))
}
