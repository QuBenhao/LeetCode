use serde_json::{json, Value};

pub struct Solution;

impl Solution {
    pub fn reverse_string(s: &mut Vec<char>) {
        
    }
}

#[cfg(feature = "solution_344")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let mut s: Vec<char> = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	Solution::reverse_string(&mut s);
	json!(s)
}
