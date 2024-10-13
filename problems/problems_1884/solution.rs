use serde_json::{json, Value};

pub struct Solution;

impl Solution {
    pub fn two_egg_drop(n: i32) -> i32 {
		return ((8 * n + 1) as f64).sqrt().ceil() as i32 / 2;
    }
}

#[cfg(feature = "solution_1884")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let n: i32 = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	json!(Solution::two_egg_drop(n))
}
