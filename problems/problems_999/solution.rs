use serde_json::{json, Value};

pub struct Solution;

impl Solution {
    pub fn num_rook_captures(board: Vec<Vec<char>>) -> i32 {
        
    }
}

#[cfg(feature = "solution_999")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let board: Vec<Vec<char>> = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	json!(Solution::num_rook_captures(board))
}
