use serde_json::{json, Value};

pub struct Solution;

impl Solution {
    pub fn max_candies(status: Vec<i32>, candies: Vec<i32>, keys: Vec<Vec<i32>>, contained_boxes: Vec<Vec<i32>>, initial_boxes: Vec<i32>) -> i32 {
        
    }
}

#[cfg(feature = "solution_1298")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let status: Vec<i32> = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	let candies: Vec<i32> = serde_json::from_str(&input_values[1]).expect("Failed to parse input");
	let keys: Vec<Vec<i32>> = serde_json::from_str(&input_values[2]).expect("Failed to parse input");
	let contained_boxes: Vec<Vec<i32>> = serde_json::from_str(&input_values[3]).expect("Failed to parse input");
	let initial_boxes: Vec<i32> = serde_json::from_str(&input_values[4]).expect("Failed to parse input");
	json!(Solution::max_candies(status, candies, keys, contained_boxes, initial_boxes))
}
