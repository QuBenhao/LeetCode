use serde_json::{json, Value};

pub struct Solution;

impl Solution {
    pub fn brace_expansion_ii(expression: String) -> Vec<String> {
        
    }
}

#[cfg(feature = "solution_1096")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let expression: String = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	json!(Solution::brace_expansion_ii(expression))
}
