#![allow(non_snake_case)]
use serde_json::{json, Value};

pub struct Solution;

impl Solution {
    pub fn ladder_length(begin_word: String, end_word: String, word_list: Vec<String>) -> i32 {

    }
}

#[cfg(feature = "solution_LCR_108")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let begin_word: String = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	let end_word: String = serde_json::from_str(&input_values[1]).expect("Failed to parse input");
	let word_list: Vec<String> = serde_json::from_str(&input_values[2]).expect("Failed to parse input");
	json!(Solution::ladder_length(begin_word, end_word, word_list))
}
