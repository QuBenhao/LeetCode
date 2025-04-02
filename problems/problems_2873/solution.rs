use serde_json::{json, Value};

pub struct Solution;

impl Solution {
    pub fn maximum_triplet_value(nums: Vec<i32>) -> i64 {
		use std::cmp::max;
        let mut ans = 0i64;
		let n = nums.len();
		let mut suf_max = vec![0; n];
		suf_max[n - 1] = nums[n - 1];
		for i in (0..n - 1).rev() {
			suf_max[i] = max(suf_max[i + 1], nums[i]);
		}
		let mut pre_max = nums[0];
		for j in 1..n - 1 {
			ans = max(ans, (pre_max - nums[j]) as i64 * suf_max[j + 1] as i64);
			pre_max = max(pre_max, nums[j]);
		}
		ans
    }
}

#[cfg(feature = "solution_2873")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let nums: Vec<i32> = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	json!(Solution::maximum_triplet_value(nums))
}
