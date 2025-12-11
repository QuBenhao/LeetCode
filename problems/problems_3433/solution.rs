use serde_json::{json, Value};

pub struct Solution;

impl Solution {
    pub fn count_mentions(number_of_users: i32, events: Vec<Vec<String>>) -> Vec<i32> {
        
    }
}

#[cfg(feature = "solution_3433")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let number_of_users: i32 = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	let events: Vec<Vec<String>> = serde_json::from_str(&input_values[1]).expect("Failed to parse input");
	json!(Solution::count_mentions(number_of_users, events))
}
