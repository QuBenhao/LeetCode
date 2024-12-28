use serde_json::{json, Value};

pub struct Solution;

impl Solution {
    pub fn rank_teams(votes: Vec<String>) -> String {
        
    }
}

#[cfg(feature = "solution_1366")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let votes: Vec<String> = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	json!(Solution::rank_teams(votes))
}
