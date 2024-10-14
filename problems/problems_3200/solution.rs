use serde_json::{json, Value};

pub struct Solution;

impl Solution {
    pub fn max_height_of_triangle(red: i32, blue: i32) -> i32 {

    }
}

#[cfg(feature = "solution_3200")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let red: i32 = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	let blue: i32 = serde_json::from_str(&input_values[1]).expect("Failed to parse input");
	json!(Solution::max_height_of_triangle(red, blue))
}
