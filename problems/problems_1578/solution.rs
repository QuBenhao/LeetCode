use serde_json::{json, Value};

pub struct Solution;

impl Solution {
    pub fn min_cost(colors: String, needed_time: Vec<i32>) -> i32 {
        
    }
}

#[cfg(feature = "solution_1578")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let colors: String = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	let needed_time: Vec<i32> = serde_json::from_str(&input_values[1]).expect("Failed to parse input");
	json!(Solution::min_cost(colors, needed_time))
}
