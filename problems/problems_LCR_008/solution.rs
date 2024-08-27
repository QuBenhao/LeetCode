#![allow(non_snake_case)]
use serde_json::{json, Value};

pub struct Solution;

use std::collections::VecDeque;
impl Solution {
    pub fn min_sub_array_len(target: i32, nums: Vec<i32>) -> i32 {
		let n = nums.len();
		let mut ans = n + 1;
		let mut queue = VecDeque::new();
		let mut sum = 0;
		for num in nums {
			queue.push_back(num);
			sum += num;
			while sum >= target {
				ans = ans.min(queue.len());
				sum -= queue.pop_front().unwrap();
			}
		}
		if ans == n + 1 {
			0
		} else {
			ans as _
		}
    }
}

#[cfg(feature = "solution_LCR_008")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let target: i32 = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	let nums: Vec<i32> = serde_json::from_str(&input_values[1]).expect("Failed to parse input");
	json!(Solution::min_sub_array_len(target, nums))
}
