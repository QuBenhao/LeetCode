use serde_json::{json, Value};

pub struct Solution;

impl Solution {
    pub fn count_good_triplets(arr: Vec<i32>, a: i32, b: i32, c: i32) -> i32 {
        
    }
}

#[cfg(feature = "solution_1534")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let arr: Vec<i32> = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	let a: i32 = serde_json::from_str(&input_values[1]).expect("Failed to parse input");
	let b: i32 = serde_json::from_str(&input_values[2]).expect("Failed to parse input");
	let c: i32 = serde_json::from_str(&input_values[3]).expect("Failed to parse input");
	json!(Solution::count_good_triplets(arr, a, b, c))
}
