#![allow(non_snake_case)]
use serde_json::{json, Value};

pub struct Solution;
use std::collections::HashMap;
impl Solution {
    pub fn subarray_sum(nums: Vec<i32>, k: i32) -> i32 {
		let mut ans = 0;
		let mut sum = 0;
		let mut map = HashMap::new();
		map.insert(0, 1);
		let n = nums.len();
		for i in 0..n {
			sum += nums[i];
			if let Some(&v) = map.get(&(sum - k)) {
				ans += v;
			}
			*map.entry(sum).or_insert(0) += 1;
		}
		ans
    }
}

#[cfg(feature = "solution_LCR_010")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let nums: Vec<i32> = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	let k: i32 = serde_json::from_str(&input_values[1]).expect("Failed to parse input");
	json!(Solution::subarray_sum(nums, k))
}
