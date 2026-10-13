use serde_json::{json, Value};

pub struct Solution;

impl Solution {
    pub fn max_sum_of_squares(num: i32, sum: i32) -> String {
        
    }
}

#[cfg(feature = "solution_3723")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let num: i32 = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	let sum: i32 = serde_json::from_str(&input_values[1]).expect("Failed to parse input");
	json!(Solution::max_sum_of_squares(num, sum))
}
