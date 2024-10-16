use serde_json::{json, Value};

pub struct Solution;

impl Solution {
    pub fn minimum_average(mut nums: Vec<i32>) -> f64 {
		nums.sort_unstable();
		let n = nums.len();
		let mut ans = nums[0] + nums[n - 1];
		for i in 1..n/2 {
			ans = ans.min(nums[i] + nums[n - i - 1]);
		}
		ans as f64 / 2.0
    }
}

#[cfg(feature = "solution_3194")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let nums: Vec<i32> = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	json!(Solution::minimum_average(nums))
}
