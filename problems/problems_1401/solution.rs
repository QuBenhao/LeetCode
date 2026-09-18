use serde_json::{json, Value};

pub struct Solution;

impl Solution {
    pub fn check_overlap(radius: i32, x_center: i32, y_center: i32, x1: i32, y1: i32, x2: i32, y2: i32) -> bool {
        
    }
}

#[cfg(feature = "solution_1401")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let radius: i32 = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	let x_center: i32 = serde_json::from_str(&input_values[1]).expect("Failed to parse input");
	let y_center: i32 = serde_json::from_str(&input_values[2]).expect("Failed to parse input");
	let x1: i32 = serde_json::from_str(&input_values[3]).expect("Failed to parse input");
	let y1: i32 = serde_json::from_str(&input_values[4]).expect("Failed to parse input");
	let x2: i32 = serde_json::from_str(&input_values[5]).expect("Failed to parse input");
	let y2: i32 = serde_json::from_str(&input_values[6]).expect("Failed to parse input");
	json!(Solution::check_overlap(radius, x_center, y_center, x1, y1, x2, y2))
}
