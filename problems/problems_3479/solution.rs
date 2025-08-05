use serde_json::{json, Value};

pub struct Solution;

impl Solution {
    pub fn num_of_unplaced_fruits(fruits: Vec<i32>, baskets: Vec<i32>) -> i32 {
        
    }
}

#[cfg(feature = "solution_3479")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let fruits: Vec<i32> = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	let baskets: Vec<i32> = serde_json::from_str(&input_values[1]).expect("Failed to parse input");
	json!(Solution::num_of_unplaced_fruits(fruits, baskets))
}
