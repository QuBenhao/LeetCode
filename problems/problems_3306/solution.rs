use serde_json::{json, Value};

pub struct Solution;

impl Solution {
    pub fn count_of_substrings(word: String, k: i32) -> i64 {
        
    }
}

#[cfg(feature = "solution_3306")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let word: String = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	let k: i32 = serde_json::from_str(&input_values[1]).expect("Failed to parse input");
	json!(Solution::count_of_substrings(word, k))
}
