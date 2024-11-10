use serde_json::{json, Value};

pub struct Solution;

impl Solution {
    pub fn min_cost(n: i32, cuts: Vec<i32>) -> i32 {
        
    }
}

#[cfg(feature = "solution_1547")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let n: i32 = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	let cuts: Vec<i32> = serde_json::from_str(&input_values[1]).expect("Failed to parse input");
	json!(Solution::min_cost(n, cuts))
}
