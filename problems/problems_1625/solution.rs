use serde_json::{json, Value};

pub struct Solution;

impl Solution {
    pub fn find_lex_smallest_string(s: String, a: i32, b: i32) -> String {
        
    }
}

#[cfg(feature = "solution_1625")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let s: String = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	let a: i32 = serde_json::from_str(&input_values[1]).expect("Failed to parse input");
	let b: i32 = serde_json::from_str(&input_values[2]).expect("Failed to parse input");
	json!(Solution::find_lex_smallest_string(s, a, b))
}
