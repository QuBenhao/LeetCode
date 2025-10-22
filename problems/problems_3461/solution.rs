use serde_json::{json, Value};

pub struct Solution;

impl Solution {
    pub fn has_same_digits(s: String) -> bool {
        
    }
}

#[cfg(feature = "solution_3461")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let s: String = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	json!(Solution::has_same_digits(s))
}
