use serde_json::{json, Value};

pub struct Solution;

impl Solution {
    pub fn find_words_containing(words: Vec<String>, x: char) -> Vec<i32> {
        
    }
}

#[cfg(feature = "solution_2942")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let words: Vec<String> = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	let x: char = serde_json::from_str(&input_values[1]).expect("Failed to parse input");
	json!(Solution::find_words_containing(words, x))
}
