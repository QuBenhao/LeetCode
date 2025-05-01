use serde_json::{json, Value};

pub struct Solution;

impl Solution {
    pub fn push_dominoes(dominoes: String) -> String {
        
    }
}

#[cfg(feature = "solution_838")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let dominoes: String = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	json!(Solution::push_dominoes(dominoes))
}
