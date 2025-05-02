use serde_json::{json, Value};

pub struct Solution;

impl Solution {
    pub fn min_domino_rotations(tops: Vec<i32>, bottoms: Vec<i32>) -> i32 {
        
    }
}

#[cfg(feature = "solution_1007")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let tops: Vec<i32> = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	let bottoms: Vec<i32> = serde_json::from_str(&input_values[1]).expect("Failed to parse input");
	json!(Solution::min_domino_rotations(tops, bottoms))
}
