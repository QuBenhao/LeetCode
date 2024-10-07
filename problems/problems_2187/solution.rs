use serde_json::{json, Value};

pub struct Solution;

impl Solution {
	pub fn minimum_time(time: Vec<i32>, total_trips: i32) -> i64 {
			let total_trips = total_trips as i64;
			let min_t = *time.iter().min().unwrap() as i64;
			let max_t = *time.iter().max().unwrap() as i64;
			let avg = (total_trips - 1) / time.len() as i64 + 1;
			// 循环不变量：check(left) 恒为 false
			let mut left = min_t * avg - 1;
			// 循环不变量：check(right) 恒为 true
			let mut right = (max_t * avg).min(min_t * total_trips);
			while left + 1 < right { // 开区间 (left, right) 不为空
					let mid = (left + right) / 2;
					let mut sum = 0;
					for &t in &time {
							sum += mid / t as i64;
					}
					if sum >= total_trips {
							right = mid; // 缩小二分区间为 (left, mid)
					} else {
							left = mid; // 缩小二分区间为 (mid, right)
					}
			}
			// 此时 left 等于 right-1
			// check(left) = false 且 check(right) = true，所以答案是 right
			right // 最小的 true
	}
}

#[cfg(feature = "solution_2187")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let time: Vec<i32> = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	let total_trips: i32 = serde_json::from_str(&input_values[1]).expect("Failed to parse input");
	json!(Solution::minimum_time(time, total_trips))
}
