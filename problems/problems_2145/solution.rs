use serde_json::{json, Value};

pub struct Solution;

impl Solution {
    pub fn number_of_arrays(differences: Vec<i32>, lower: i32, upper: i32) -> i32 {
        
    }
}

#[cfg(feature = "solution_2145")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let differences: Vec<i32> = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	let lower: i32 = serde_json::from_str(&input_values[1]).expect("Failed to parse input");
	let upper: i32 = serde_json::from_str(&input_values[2]).expect("Failed to parse input");
	json!(Solution::number_of_arrays(differences, lower, upper))
}
