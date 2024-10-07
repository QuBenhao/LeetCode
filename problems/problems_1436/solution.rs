use serde_json::{json, Value};

pub struct Solution;

impl Solution {
    pub fn dest_city(paths: Vec<Vec<String>>) -> String {

    }
}

#[cfg(feature = "solution_1436")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let paths: Vec<Vec<String>> = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	json!(Solution::dest_city(paths))
}
