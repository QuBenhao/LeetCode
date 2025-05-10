use serde_json::{json, Value};

pub struct Solution;

impl Solution {
    pub fn three_consecutive_odds(arr: Vec<i32>) -> bool {
        
    }
}

#[cfg(feature = "solution_1550")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let arr: Vec<i32> = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	json!(Solution::three_consecutive_odds(arr))
}
