use serde_json::{json, Value};

pub struct Solution;

impl Solution {
    pub fn generate_key(num1: i32, num2: i32, num3: i32) -> i32 {
        
    }
}

#[cfg(feature = "solution_3270")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let num1: i32 = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	let num2: i32 = serde_json::from_str(&input_values[1]).expect("Failed to parse input");
	let num3: i32 = serde_json::from_str(&input_values[2]).expect("Failed to parse input");
	json!(Solution::generate_key(num1, num2, num3))
}
