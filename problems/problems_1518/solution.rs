use serde_json::{json, Value};

pub struct Solution;

impl Solution {
    pub fn num_water_bottles(num_bottles: i32, num_exchange: i32) -> i32 {
        
    }
}

#[cfg(feature = "solution_1518")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let num_bottles: i32 = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	let num_exchange: i32 = serde_json::from_str(&input_values[1]).expect("Failed to parse input");
	json!(Solution::num_water_bottles(num_bottles, num_exchange))
}
