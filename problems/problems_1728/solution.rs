use serde_json::{json, Value};

pub struct Solution;

impl Solution {
    pub fn can_mouse_win(grid: Vec<String>, cat_jump: i32, mouse_jump: i32) -> bool {
        
    }
}

#[cfg(feature = "solution_1728")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let grid: Vec<String> = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	let cat_jump: i32 = serde_json::from_str(&input_values[1]).expect("Failed to parse input");
	let mouse_jump: i32 = serde_json::from_str(&input_values[2]).expect("Failed to parse input");
	json!(Solution::can_mouse_win(grid, cat_jump, mouse_jump))
}
