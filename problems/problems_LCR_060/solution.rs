#![allow(non_snake_case)]
use serde_json::{json, Value};

pub struct Solution;

use std::collections::{HashMap, BinaryHeap};
impl Solution {
    pub fn top_k_frequent(nums: Vec<i32>, k: i32) -> Vec<i32> {
		let mut map = HashMap::new();
		for num in nums {
			*map.entry(num).or_insert(0) += 1;
		}
		let mut heap = BinaryHeap::new();
		for (num, count) in map {
			heap.push((count, num));
		}
		let mut res = Vec::new();
		for _ in 0..k {
			res.push(heap.pop().unwrap().1);
		}
		res
    }
}

#[cfg(feature = "solution_LCR_060")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let nums: Vec<i32> = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	let k: i32 = serde_json::from_str(&input_values[1]).expect("Failed to parse input");
	json!(Solution::top_k_frequent(nums, k))
}
