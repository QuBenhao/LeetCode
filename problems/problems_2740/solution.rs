use serde_json::{json, Value};

pub struct Solution;

impl Solution {
    pub fn find_value_of_partition(nums: Vec<i32>) -> i32 {
		let mut nums = nums;
		nums.sort_unstable();
		nums.windows(2).map(|x| x[1] - x[0]).min().unwrap()
    }
}

#[cfg(feature = "solution_2740")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let nums: Vec<i32> = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	json!(Solution::find_value_of_partition(nums))
}
