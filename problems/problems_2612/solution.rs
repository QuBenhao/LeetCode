use serde_json::{json, Value};

pub struct Solution;

impl Solution {
    pub fn min_reverse_operations(n: i32, p: i32, banned: Vec<i32>, k: i32) -> Vec<i32> {
        
    }
}

#[cfg(feature = "solution_2612")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let n: i32 = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	let p: i32 = serde_json::from_str(&input_values[1]).expect("Failed to parse input");
	let banned: Vec<i32> = serde_json::from_str(&input_values[2]).expect("Failed to parse input");
	let k: i32 = serde_json::from_str(&input_values[3]).expect("Failed to parse input");
	json!(Solution::min_reverse_operations(n, p, banned, k))
}
