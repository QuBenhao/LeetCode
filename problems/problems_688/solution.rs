use serde_json::{json, Value};

pub struct Solution;

impl Solution {
    pub fn knight_probability(n: i32, k: i32, row: i32, column: i32) -> f64 {
        
    }
}

#[cfg(feature = "solution_688")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let n: i32 = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	let k: i32 = serde_json::from_str(&input_values[1]).expect("Failed to parse input");
	let row: i32 = serde_json::from_str(&input_values[2]).expect("Failed to parse input");
	let column: i32 = serde_json::from_str(&input_values[3]).expect("Failed to parse input");
	json!(Solution::knight_probability(n, k, row, column))
}
