use serde_json::{json, Value};

pub struct Solution;

impl Solution {
    pub fn latest_day_to_cross(row: i32, col: i32, cells: Vec<Vec<i32>>) -> i32 {
        
    }
}

#[cfg(feature = "solution_1970")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let row: i32 = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	let col: i32 = serde_json::from_str(&input_values[1]).expect("Failed to parse input");
	let cells: Vec<Vec<i32>> = serde_json::from_str(&input_values[2]).expect("Failed to parse input");
	json!(Solution::latest_day_to_cross(row, col, cells))
}
