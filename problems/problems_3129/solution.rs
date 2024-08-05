use serde_json::{json, Value};

pub struct Solution;

impl Solution {
    pub fn number_of_stable_arrays(zero: i32, one: i32, limit: i32) -> i32 {

    }
}

#[cfg(feature = "solution_3129")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let zero: i32 = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	let one: i32 = serde_json::from_str(&input_values[1]).expect("Failed to parse input");
	let limit: i32 = serde_json::from_str(&input_values[2]).expect("Failed to parse input");
	json!(Solution::number_of_stable_arrays(zero, one, limit))
}
