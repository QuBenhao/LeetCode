use serde_json::{json, Value};

pub struct Solution;

impl Solution {
    pub fn divide_string(s: String, k: i32, fill: char) -> Vec<String> {
        
    }
}

#[cfg(feature = "solution_2138")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let s: String = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	let k: i32 = serde_json::from_str(&input_values[1]).expect("Failed to parse input");
	let fill: char = serde_json::from_str(&input_values[2]).expect("Failed to parse input");
	json!(Solution::divide_string(s, k, fill))
}
