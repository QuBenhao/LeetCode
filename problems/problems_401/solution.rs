use serde_json::{json, Value};

pub struct Solution;

impl Solution {
    pub fn read_binary_watch(turned_on: i32) -> Vec<String> {
        
    }
}

#[cfg(feature = "solution_401")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let turned_on: i32 = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	json!(Solution::read_binary_watch(turned_on))
}
