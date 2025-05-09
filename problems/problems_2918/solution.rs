use serde_json::{json, Value};

pub struct Solution;

impl Solution {
    pub fn min_sum(nums1: Vec<i32>, nums2: Vec<i32>) -> i64 {
        
    }
}

#[cfg(feature = "solution_2918")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let nums1: Vec<i32> = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	let nums2: Vec<i32> = serde_json::from_str(&input_values[1]).expect("Failed to parse input");
	json!(Solution::min_sum(nums1, nums2))
}
