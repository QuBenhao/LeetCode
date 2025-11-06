use serde_json::{json, Value};

pub struct Solution;

impl Solution {
    pub fn max_power(stations: Vec<i32>, r: i32, k: i32) -> i64 {
        
    }
}

#[cfg(feature = "solution_2528")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let stations: Vec<i32> = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	let r: i32 = serde_json::from_str(&input_values[1]).expect("Failed to parse input");
	let k: i32 = serde_json::from_str(&input_values[2]).expect("Failed to parse input");
	json!(Solution::max_power(stations, r, k))
}
