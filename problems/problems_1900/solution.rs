use serde_json::{json, Value};

pub struct Solution;

impl Solution {
    pub fn earliest_and_latest(n: i32, first_player: i32, second_player: i32) -> Vec<i32> {
        
    }
}

#[cfg(feature = "solution_1900")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let n: i32 = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	let first_player: i32 = serde_json::from_str(&input_values[1]).expect("Failed to parse input");
	let second_player: i32 = serde_json::from_str(&input_values[2]).expect("Failed to parse input");
	json!(Solution::earliest_and_latest(n, first_player, second_player))
}
