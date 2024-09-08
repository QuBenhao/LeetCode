#![allow(non_snake_case)]
use serde_json::{json, Value};

pub struct Solution;

impl Solution {
    pub fn num_subarray_product_less_than_k(nums: Vec<i32>, k: i32) -> i32 {
		let mut ans: i32 = 0;
		let mut cur: i32 = 1;
		let mut left: usize = 0;
		for right in 0..nums.len() {
			cur *= nums[right];
			while cur >= k && left <= right {
				cur /= nums[left];
				left += 1;
			}
			ans += right as i32 - left as i32 + 1;
		}
		ans
    }
}

#[cfg(feature = "solution_LCR_009")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let nums: Vec<i32> = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	let k: i32 = serde_json::from_str(&input_values[1]).expect("Failed to parse input");
	json!(Solution::num_subarray_product_less_than_k(nums, k))
}
