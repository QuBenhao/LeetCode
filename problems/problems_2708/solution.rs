use serde_json::{json, Value};

pub struct Solution;

impl Solution {
    pub fn max_strength(nums: Vec<i32>) -> i64 {
		let mut mx: i64 = nums[0] as i64;
		let mut mn: i64 = nums[0] as i64;
		for i in 1..nums.len() {
			let tmp_mx = mx;
			let tmp_mn = mn;
			let num = nums[i] as i64;
			mx = mx.max(num).max(num * tmp_mx).max(num * mn);
			mn = mn.min(num).min(num * tmp_mn).min(num * tmp_mx);
		}
		mx
    }
}

#[cfg(feature = "solution_2708")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let nums: Vec<i32> = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	json!(Solution::max_strength(nums))
}
