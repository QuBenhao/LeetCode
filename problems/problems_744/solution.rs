use serde_json::{json, Value};

pub struct Solution;

impl Solution {
    pub fn next_greatest_letter(letters: Vec<char>, target: char) -> char {
        
    }
}

#[cfg(feature = "solution_744")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let letters: Vec<char> = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	let target: char = serde_json::from_str(&input_values[1]).expect("Failed to parse input");
	json!(Solution::next_greatest_letter(letters, target))
}
