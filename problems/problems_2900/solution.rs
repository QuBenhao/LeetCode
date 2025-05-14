use serde_json::{json, Value};

pub struct Solution;

impl Solution {
    pub fn get_longest_subsequence(words: Vec<String>, groups: Vec<i32>) -> Vec<String> {
        
    }
}

#[cfg(feature = "solution_2900")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let words: Vec<String> = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	let groups: Vec<i32> = serde_json::from_str(&input_values[1]).expect("Failed to parse input");
	json!(Solution::get_longest_subsequence(words, groups))
}
