use serde_json::{json, Value};

pub struct Solution;

impl Solution {
    pub fn is_array_special(nums: Vec<i32>, queries: Vec<Vec<i32>>) -> Vec<bool> {
		let n = nums.len();
		let mut pre_sum: Vec<i32> = vec![0; n];
		for i in 0..n - 1 {
			pre_sum[i + 1] = pre_sum[i] + ((nums[i] & 1) != (nums[i + 1] & 1)) as i32;
		}
		let mut res: Vec<bool> = Vec::new();
		for query in queries {
			let l = query[0];
			let r = query[1];
			res.push(pre_sum[r as usize] - pre_sum[l as usize] == r - l);
		}
		res
    }
}

#[cfg(feature = "solution_3152")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let nums: Vec<i32> = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	let queries: Vec<Vec<i32>> = serde_json::from_str(&input_values[1]).expect("Failed to parse input");
	json!(Solution::is_array_special(nums, queries))
}
