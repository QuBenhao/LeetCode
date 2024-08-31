use serde_json::{json, Value};

pub struct Solution;

impl Solution {
    pub fn product_except_self(nums: Vec<i32>) -> Vec<i32> {
		let n = nums.len();
		let mut res = vec![1; n];
		for i in 1..n {
			res[i] = res[i-1] * nums[i-1];
		}
		let mut right = 1;
		for i in (0..n).rev() {
			res[i] *= right;
			right *= nums[i];
		}
		res
    }
}

#[cfg(feature = "solution_238")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let nums: Vec<i32> = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	json!(Solution::product_except_self(nums))
}
