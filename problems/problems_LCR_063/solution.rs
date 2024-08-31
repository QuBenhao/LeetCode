#![allow(non_snake_case)]
use serde_json::{json, Value};

pub struct Solution;

impl Solution {
    pub fn replace_words(dictionary: Vec<String>, sentence: String) -> String {

    }
}

#[cfg(feature = "solution_LCR_063")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let dictionary: Vec<String> = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	let sentence: String = serde_json::from_str(&input_values[1]).expect("Failed to parse input");
	json!(Solution::replace_words(dictionary, sentence))
}
