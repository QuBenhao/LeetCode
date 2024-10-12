use serde_json::{json, Value};

pub struct Solution;
use std::collections::HashSet;

impl Solution {
    pub fn duplicate_numbers_xor(nums: Vec<i32>) -> i32 {
		let mut ans: i32 = 0;
		let mut explored: HashSet<i32> = HashSet::new();
		for num in nums {
			if explored.contains(&num) {
				ans ^= num;
			} else {
				explored.insert(num);
			}
		}
		ans
    }
}

#[cfg(feature = "solution_3158")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let nums: Vec<i32> = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	json!(Solution::duplicate_numbers_xor(nums))
}
