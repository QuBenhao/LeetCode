use serde_json::{json, Value};

pub struct Solution;

impl Solution {
    pub fn cal_points(operations: Vec<String>) -> i32 {

    }
}

#[cfg(feature = "solution_682")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let operations: Vec<String> = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	json!(Solution::cal_points(operations))
}
