#![allow(non_snake_case)]
use serde_json::{json, Value};

pub struct Solution;

use std::cmp::min;
impl Solution {
    pub fn min_cost_climbing_stairs(cost: Vec<i32>) -> i32 {
		let n = cost.len();
		let mut dp = vec![0; 3];
		for i in 2..n + 1 {
			dp[i % 3] = min(dp[(i - 1) % 3] + cost[i - 1], dp[(i - 2) % 3] + cost[i - 2]);
		}
		dp[n % 3]
    }
}

#[cfg(feature = "solution_LCR_088")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let cost: Vec<i32> = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	json!(Solution::min_cost_climbing_stairs(cost))
}
