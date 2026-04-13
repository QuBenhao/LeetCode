use serde_json::{json, Value};

pub struct Solution;

impl Solution {
    pub fn minimum_total_distance(robot: Vec<i32>, factory: Vec<Vec<i32>>) -> i64 {
        
    }
}

#[cfg(feature = "solution_2463")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let robot: Vec<i32> = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	let factory: Vec<Vec<i32>> = serde_json::from_str(&input_values[1]).expect("Failed to parse input");
	json!(Solution::minimum_total_distance(robot, factory))
}
