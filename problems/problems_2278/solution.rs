use serde_json::{json, Value};

pub struct Solution;

impl Solution {
    pub fn percentage_letter(s: String, letter: char) -> i32 {
        
    }
}

#[cfg(feature = "solution_2278")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let s: String = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	let letter: char = serde_json::from_str(&input_values[1]).expect("Failed to parse input");
	json!(Solution::percentage_letter(s, letter))
}
