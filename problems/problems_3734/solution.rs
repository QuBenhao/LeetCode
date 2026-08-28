use serde_json::{json, Value};

pub struct Solution;

impl Solution {
    pub fn lex_palindromic_permutation(s: String, target: String) -> String {
        
    }
}

#[cfg(feature = "solution_3734")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let s: String = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	let target: String = serde_json::from_str(&input_values[1]).expect("Failed to parse input");
	json!(Solution::lex_palindromic_permutation(s, target))
}
