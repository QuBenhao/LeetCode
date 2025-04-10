use serde_json::{json, Value};

pub struct Solution;

impl Solution {
    pub fn count_symmetric_integers(low: i32, high: i32) -> i32 {
        
    }
}

#[cfg(feature = "solution_2843")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let low: i32 = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	let high: i32 = serde_json::from_str(&input_values[1]).expect("Failed to parse input");
	json!(Solution::count_symmetric_integers(low, high))
}
