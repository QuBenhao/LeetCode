use serde_json::{json, Value};

pub struct Solution;

impl Solution {
    pub fn number_of_powerful_int(start: i64, finish: i64, limit: i32, s: String) -> i64 {
        
    }
}

#[cfg(feature = "solution_2999")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let start: i64 = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	let finish: i64 = serde_json::from_str(&input_values[1]).expect("Failed to parse input");
	let limit: i32 = serde_json::from_str(&input_values[2]).expect("Failed to parse input");
	let s: String = serde_json::from_str(&input_values[3]).expect("Failed to parse input");
	json!(Solution::number_of_powerful_int(start, finish, limit, s))
}
