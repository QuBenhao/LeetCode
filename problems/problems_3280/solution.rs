use serde_json::{json, Value};

pub struct Solution;

impl Solution {
    pub fn convert_date_to_binary(date: String) -> String {
        
    }
}

#[cfg(feature = "solution_3280")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let date: String = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	json!(Solution::convert_date_to_binary(date))
}
