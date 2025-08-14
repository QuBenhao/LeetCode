use serde_json::{json, Value};

pub struct Solution;

impl Solution {
    pub fn is_power_of_four(n: i32) -> bool {
        
    }
}

#[cfg(feature = "solution_342")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let n: i32 = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	json!(Solution::is_power_of_four(n))
}
