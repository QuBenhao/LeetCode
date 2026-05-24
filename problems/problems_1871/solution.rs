use serde_json::{json, Value};

pub struct Solution;

impl Solution {
    pub fn can_reach(s: String, min_jump: i32, max_jump: i32) -> bool {
        
    }
}

#[cfg(feature = "solution_1871")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let s: String = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	let min_jump: i32 = serde_json::from_str(&input_values[1]).expect("Failed to parse input");
	let max_jump: i32 = serde_json::from_str(&input_values[2]).expect("Failed to parse input");
	json!(Solution::can_reach(s, min_jump, max_jump))
}
