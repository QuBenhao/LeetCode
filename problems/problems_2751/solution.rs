use serde_json::{json, Value};

pub struct Solution;

impl Solution {
    pub fn survived_robots_healths(positions: Vec<i32>, healths: Vec<i32>, directions: String) -> Vec<i32> {
        
    }
}

#[cfg(feature = "solution_2751")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let positions: Vec<i32> = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	let healths: Vec<i32> = serde_json::from_str(&input_values[1]).expect("Failed to parse input");
	let directions: String = serde_json::from_str(&input_values[2]).expect("Failed to parse input");
	json!(Solution::survived_robots_healths(positions, healths, directions))
}
