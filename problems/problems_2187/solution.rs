use serde_json::{json, Value};

pub struct Solution;

impl Solution {
	pub fn minimum_time(time: Vec<i32>, total_trips: i32) -> i64 {
			let total_trips = total_trips as i64;
			let min_t = *time.iter().min().unwrap() as i64;
			let max_t = *time.iter().max().unwrap() as i64;
			let avg = (total_trips - 1) / time.len() as i64 + 1;
			// Loop invariant: check(left) is always false
			let mut left = min_t * avg - 1;
			// Loop invariant: check(right) is always true
			let mut right = (max_t * avg).min(min_t * total_trips);
			while left + 1 < right { // The open interval (left, right) is nonempty
					let mid = (left + right) / 2;
					let mut sum = 0;
					for &t in &time {
							sum += mid / t as i64;
					}
					if sum >= total_trips {
							right = mid; // Shrink the binary-search interval to (left, mid)
					} else {
							left = mid; // Shrink the binary-search interval to (mid, right)
					}
			}
			// Now left equals right-1
			// check(left) = false and check(right) = true, so the answer is right
			right // The smallest value for which the predicate is true
	}
}

#[cfg(feature = "solution_2187")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let time: Vec<i32> = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	let total_trips: i32 = serde_json::from_str(&input_values[1]).expect("Failed to parse input");
	json!(Solution::minimum_time(time, total_trips))
}
