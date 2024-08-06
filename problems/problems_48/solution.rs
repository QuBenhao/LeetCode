use serde_json::{json, Value};

pub struct Solution;

impl Solution {
    pub fn rotate(matrix: &mut Vec<Vec<i32>>) {

    }
}

#[cfg(feature = "solution_48")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let matrix: &mut Vec<Vec<i32>> = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	Solution::rotate(matrix);
	matrix
}
