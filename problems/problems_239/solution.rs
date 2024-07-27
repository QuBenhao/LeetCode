use serde_json::{json, Value};

pub struct Solution;

use std::collections::VecDeque;
impl Solution {
    pub fn max_sliding_window(nums: Vec<i32>, k: i32) -> Vec<i32> {
		let mut res = vec![];
		let mut deque = VecDeque::new();
		for i in 0..nums.len() {
			while !deque.is_empty() && nums[*deque.back().unwrap()] <= nums[i] {
				deque.pop_back();
			}
			deque.push_back(i);
			if i - deque.front().unwrap() == k as usize {
				deque.pop_front();
			}
			if i >= k as usize - 1 {
				res.push(nums[*deque.front().unwrap()]);
			}
		}
		res
    }
}

#[cfg(feature = "solution_239")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let nums: Vec<i32> = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	let k: i32 = serde_json::from_str(&input_values[1]).expect("Failed to parse input");
	json!(Solution::max_sliding_window(nums, k))
}
