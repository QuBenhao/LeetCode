use serde_json::{json, Value};

pub struct Solution;

impl Solution {
    pub fn min_window(s: String, t: String) -> String {

    }
}

#[cfg(feature = "solution_76")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let s: String = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	let t: String = serde_json::from_str(&input_values[1]).expect("Failed to parse input");
	json!(Solution::min_window(s, t))
}
