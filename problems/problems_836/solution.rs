use serde_json::{json, Value};

pub struct Solution;

impl Solution {
    pub fn is_rectangle_overlap(rec1: Vec<i32>, rec2: Vec<i32>) -> bool {
        
    }
}

#[cfg(feature = "solution_836")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let rec1: Vec<i32> = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	let rec2: Vec<i32> = serde_json::from_str(&input_values[1]).expect("Failed to parse input");
	json!(Solution::is_rectangle_overlap(rec1, rec2))
}
