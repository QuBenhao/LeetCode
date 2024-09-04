use serde_json::{json, Value};

pub struct Solution;

impl Solution {
    pub fn count_ways(nums: Vec<i32>) -> i32 {
		let mut nums = nums;
		nums.sort_unstable();
		let mut ans = 1;
		if nums[0] > 0 {
			ans += 1;
		}
		for i in 1..nums.len() {
			if nums[i - 1] < i as i32 && nums[i] > i as i32 {
				ans += 1;
			}
		}
		ans
    }
}

#[cfg(feature = "solution_2860")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let nums: Vec<i32> = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	json!(Solution::count_ways(nums))
}
