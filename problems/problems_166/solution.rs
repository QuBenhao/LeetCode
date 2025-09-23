use serde_json::{json, Value};

pub struct Solution;

impl Solution {
    pub fn fraction_to_decimal(numerator: i32, denominator: i32) -> String {
        
    }
}

#[cfg(feature = "solution_166")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let numerator: i32 = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	let denominator: i32 = serde_json::from_str(&input_values[1]).expect("Failed to parse input");
	json!(Solution::fraction_to_decimal(numerator, denominator))
}
