use serde_json::{json, Value};

pub struct Solution;

impl Solution {
    pub fn can_be_typed_words(text: String, broken_letters: String) -> i32 {
        
    }
}

#[cfg(feature = "solution_1935")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let text: String = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	let broken_letters: String = serde_json::from_str(&input_values[1]).expect("Failed to parse input");
	json!(Solution::can_be_typed_words(text, broken_letters))
}
