use serde_json::{json, Value};

pub struct Solution;

impl Solution {
    pub fn find_closest(x: i32, y: i32, z: i32) -> i32 {
        
    }
}

#[cfg(feature = "solution_3516")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let x: i32 = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	let y: i32 = serde_json::from_str(&input_values[1]).expect("Failed to parse input");
	let z: i32 = serde_json::from_str(&input_values[2]).expect("Failed to parse input");
	json!(Solution::find_closest(x, y, z))
}
