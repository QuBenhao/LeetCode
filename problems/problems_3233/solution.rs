use serde_json::{json, Value};

pub struct Solution;

impl Solution {
    pub fn non_special_count(l: i32, r: i32) -> i32 {
        
    }
}

#[cfg(feature = "solution_3233")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let l: i32 = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	let r: i32 = serde_json::from_str(&input_values[1]).expect("Failed to parse input");
	json!(Solution::non_special_count(l, r))
}
