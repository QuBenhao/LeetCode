use serde_json::{json, Value};

pub struct Solution;

use std::collections::vec_deque::VecDeque;
impl Solution {
    pub fn maximum_robots(charge_times: Vec<i32>, running_costs: Vec<i32>, budget: i64) -> i32 {
		let n = charge_times.len();
		let mut left = 0;
		let mut right = n;
		let check = |mid: usize| -> bool {
			let mut sum: i64 = 0;
			let mut q: VecDeque<usize> = VecDeque::new();
			for i in 0..n {
				while !q.is_empty() && charge_times[*q.back().unwrap()] <= charge_times[i] {
					q.pop_back();
				}
				q.push_back(i);
				sum += running_costs[i] as i64;
				if i >= q[0] + mid {
					q.pop_front();
				}
				if i >= mid - 1 {
					if sum * mid as i64 + charge_times[q[0]] as i64 <= budget {
						return true;
					}
					if let Some(index) = i.checked_sub(mid - 1) {
						sum -= running_costs[index] as i64;
					}
				}
			}
			false
		};
		while left < right {
			let mid = (left + right + 1) / 2;
			if !check(mid) {
				right = mid - 1;
			} else {
				left = mid;
			}
		}
		left as i32
    }
}

#[cfg(feature = "solution_2398")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let charge_times: Vec<i32> = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	let running_costs: Vec<i32> = serde_json::from_str(&input_values[1]).expect("Failed to parse input");
	let budget: i64 = serde_json::from_str(&input_values[2]).expect("Failed to parse input");
	json!(Solution::maximum_robots(charge_times, running_costs, budget))
}
