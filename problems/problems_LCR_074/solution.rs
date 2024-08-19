#![allow(non_snake_case)]
use serde_json::{json, Value};

pub struct Solution;

impl Solution {
    pub fn merge(intervals: Vec<Vec<i32>>) -> Vec<Vec<i32>> {
		let mut intervals = intervals;
		intervals.sort_unstable();
		let mut res: Vec<Vec<i32>> = vec![];
		for interval in intervals {
			if res.is_empty() || res.last().unwrap()[1] < interval[0] {
				res.push(interval);
			} else {
				res.last_mut().unwrap()[1] = res.last().unwrap()[1].max(interval[1]);
			}
		}
		res
    }
}

#[cfg(feature = "solution_LCR_074")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let intervals: Vec<Vec<i32>> = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	json!(Solution::merge(intervals))
}
