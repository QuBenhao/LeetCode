use serde_json::{json, Value};

pub struct Solution;

impl Solution {
    pub fn count_prime_set_bits(left: i32, right: i32) -> i32 {

    }
}

#[cfg(feature = "solution_762")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let left: i32 = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	let right: i32 = serde_json::from_str(&input_values[1]).expect("Failed to parse input");
	json!(Solution::count_prime_set_bits(left, right))
}
