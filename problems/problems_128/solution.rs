use serde_json::{json, Value};

pub struct Solution;

use std::collections::HashMap;
impl Solution {
    pub fn longest_consecutive(nums: Vec<i32>) -> i32 {
		let mut map: HashMap<i32, i32> = HashMap::new();
		let mut res = 0;
		for num in nums {
			if map.contains_key(&num) {
				continue;
			}
			let left = *map.get(&(num - 1)).unwrap_or(&0);
			let right = *map.get(&(num + 1)).unwrap_or(&0);
			let sum = left + right + 1;
			map.insert(num, sum);
			map.insert(num - left, sum);
			map.insert(num + right, sum);
			res = res.max(sum);
		}
		res
    }
}

#[cfg(feature = "solution_128")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let nums: Vec<i32> = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	json!(Solution::longest_consecutive(nums))
}
