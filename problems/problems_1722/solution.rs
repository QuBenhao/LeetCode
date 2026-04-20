use serde_json::{json, Value};

pub struct Solution;

impl Solution {
    pub fn minimum_hamming_distance(source: Vec<i32>, target: Vec<i32>, allowed_swaps: Vec<Vec<i32>>) -> i32 {
        
    }
}

#[cfg(feature = "solution_1722")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let source: Vec<i32> = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	let target: Vec<i32> = serde_json::from_str(&input_values[1]).expect("Failed to parse input");
	let allowed_swaps: Vec<Vec<i32>> = serde_json::from_str(&input_values[2]).expect("Failed to parse input");
	json!(Solution::minimum_hamming_distance(source, target, allowed_swaps))
}
