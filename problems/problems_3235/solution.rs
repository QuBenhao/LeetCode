use serde_json::{json, Value};

pub struct Solution;

impl Solution {
    pub fn can_reach_corner(x_corner: i32, y_corner: i32, circles: Vec<Vec<i32>>) -> bool {
        
    }
}

#[cfg(feature = "solution_3235")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let x_corner: i32 = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	let y_corner: i32 = serde_json::from_str(&input_values[1]).expect("Failed to parse input");
	let circles: Vec<Vec<i32>> = serde_json::from_str(&input_values[2]).expect("Failed to parse input");
	json!(Solution::can_reach_corner(x_corner, y_corner, circles))
}
