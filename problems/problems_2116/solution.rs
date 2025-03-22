use serde_json::{json, Value};

pub struct Solution;

impl Solution {
    pub fn can_be_valid(s: String, locked: String) -> bool {
        
    }
}

#[cfg(feature = "solution_2116")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let s: String = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	let locked: String = serde_json::from_str(&input_values[1]).expect("Failed to parse input");
	json!(Solution::can_be_valid(s, locked))
}
