use serde_json::{json, Value};

pub struct Solution;

impl Solution {
    pub fn exist(board: Vec<Vec<char>>, word: String) -> bool {

    }
}

#[cfg(feature = "solution_79")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let board: Vec<Vec<char>> = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	let word: String = serde_json::from_str(&input_values[1]).expect("Failed to parse input");
	json!(Solution::exist(board, word))
}
