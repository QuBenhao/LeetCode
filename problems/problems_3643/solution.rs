use serde_json::{json, Value};

pub struct Solution;

impl Solution {
    pub fn reverse_submatrix(grid: Vec<Vec<i32>>, x: i32, y: i32, k: i32) -> Vec<Vec<i32>> {
        
    }
}

#[cfg(feature = "solution_3643")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let grid: Vec<Vec<i32>> = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	let x: i32 = serde_json::from_str(&input_values[1]).expect("Failed to parse input");
	let y: i32 = serde_json::from_str(&input_values[2]).expect("Failed to parse input");
	let k: i32 = serde_json::from_str(&input_values[3]).expect("Failed to parse input");
	json!(Solution::reverse_submatrix(grid, x, y, k))
}
