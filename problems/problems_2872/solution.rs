use serde_json::{json, Value};

pub struct Solution;

impl Solution {
    pub fn max_k_divisible_components(n: i32, edges: Vec<Vec<i32>>, values: Vec<i32>, k: i32) -> i32 {
        
    }
}

#[cfg(feature = "solution_2872")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let n: i32 = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	let edges: Vec<Vec<i32>> = serde_json::from_str(&input_values[1]).expect("Failed to parse input");
	let values: Vec<i32> = serde_json::from_str(&input_values[2]).expect("Failed to parse input");
	let k: i32 = serde_json::from_str(&input_values[3]).expect("Failed to parse input");
	json!(Solution::max_k_divisible_components(n, edges, values, k))
}
