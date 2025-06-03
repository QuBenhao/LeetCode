use serde_json::{json, Value};

pub struct Solution;

impl Solution {
    pub fn answer_string(word: String, num_friends: i32) -> String {
        
    }
}

#[cfg(feature = "solution_3403")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let word: String = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	let num_friends: i32 = serde_json::from_str(&input_values[1]).expect("Failed to parse input");
	json!(Solution::answer_string(word, num_friends))
}
