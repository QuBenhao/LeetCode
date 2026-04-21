use serde_json::{json, Value};

pub struct Solution;

impl Solution {
    pub fn two_edit_words(queries: Vec<String>, dictionary: Vec<String>) -> Vec<String> {
        
    }
}

#[cfg(feature = "solution_2452")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let queries: Vec<String> = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	let dictionary: Vec<String> = serde_json::from_str(&input_values[1]).expect("Failed to parse input");
	json!(Solution::two_edit_words(queries, dictionary))
}
