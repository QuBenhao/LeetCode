use serde_json::{json, Value};

pub struct Solution;

impl Solution {
    pub fn angle_clock(hour: i32, minutes: i32) -> f64 {
        
    }
}

#[cfg(feature = "solution_1344")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let hour: i32 = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	let minutes: i32 = serde_json::from_str(&input_values[1]).expect("Failed to parse input");
	json!(Solution::angle_clock(hour, minutes))
}
