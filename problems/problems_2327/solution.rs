use serde_json::{json, Value};

pub struct Solution;

impl Solution {
    pub fn people_aware_of_secret(n: i32, delay: i32, forget: i32) -> i32 {
        
    }
}

#[cfg(feature = "solution_2327")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let n: i32 = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	let delay: i32 = serde_json::from_str(&input_values[1]).expect("Failed to parse input");
	let forget: i32 = serde_json::from_str(&input_values[2]).expect("Failed to parse input");
	json!(Solution::people_aware_of_secret(n, delay, forget))
}
