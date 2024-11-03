use serde_json::{json, Value};

pub struct Solution;

impl Solution {
    pub fn judge_square_sum(c: i32) -> bool {
        
    }
}

#[cfg(feature = "solution_633")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let c: i32 = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	json!(Solution::judge_square_sum(c))
}
