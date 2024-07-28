use serde_json::{json, Value};

pub struct Solution;

impl Solution {
    pub fn merge(intervals: Vec<Vec<i32>>) -> Vec<Vec<i32>> {
		let mut intervals = intervals;
		intervals.sort_unstable_by(|a, b| a[0].cmp(&b[0]));
		let mut merged: Vec<Vec<i32>> = Vec::new();
		for interval in intervals {
			if let Some(last) = merged.last_mut() {
				if interval[0] <= last[1] {
					last[1] = last[1].max(interval[1]);
				} else {
					merged.push(interval);
				}
			} else {
				merged.push(interval);
			}
		}
		merged
    }
}

#[cfg(feature = "solution_56")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let intervals: Vec<Vec<i32>> = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	json!(Solution::merge(intervals))
}
