use serde_json::{json, Value};

pub struct Solution;

impl Solution {
    pub fn minimum_white_tiles(floor: String, num_carpets: i32, carpet_len: i32) -> i32 {
        
    }
}

#[cfg(feature = "solution_2209")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let floor: String = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	let num_carpets: i32 = serde_json::from_str(&input_values[1]).expect("Failed to parse input");
	let carpet_len: i32 = serde_json::from_str(&input_values[2]).expect("Failed to parse input");
	json!(Solution::minimum_white_tiles(floor, num_carpets, carpet_len))
}
