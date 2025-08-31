use serde_json::{json, Value};

pub struct Solution;

impl Solution {
    pub fn max_average_ratio(classes: Vec<Vec<i32>>, extra_students: i32) -> f64 {
        
    }
}

#[cfg(feature = "solution_1792")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let classes: Vec<Vec<i32>> = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	let extra_students: i32 = serde_json::from_str(&input_values[1]).expect("Failed to parse input");
	json!(Solution::max_average_ratio(classes, extra_students))
}
