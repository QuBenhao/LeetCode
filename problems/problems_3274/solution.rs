use serde_json::{json, Value};

pub struct Solution;

impl Solution {
    pub fn check_two_chessboards(coordinate1: String, coordinate2: String) -> bool {
        
    }
}

#[cfg(feature = "solution_3274")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let coordinate1: String = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	let coordinate2: String = serde_json::from_str(&input_values[1]).expect("Failed to parse input");
	json!(Solution::check_two_chessboards(coordinate1, coordinate2))
}
