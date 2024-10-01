use serde_json::{json, Value};

pub struct Solution;

impl Solution {
    pub fn mincost_tickets(days: Vec<i32>, costs: Vec<i32>) -> i32 {
		let n = days.len();
		let mut dp = vec![0; n + 1];
		let mut j: usize = 0;
		let mut k: usize = 0;
		let iter = days.iter().enumerate();
		for (i, &day) in iter {
			while days[j] <= day - 7 {
				j += 1;
			}
			while days[k] <= day - 30 {
				k += 1;
			}
			dp[i + 1] = (dp[j] + costs[1]).min(dp[k] + costs[2]).min(dp[i] + costs[0]);
		}
		dp[n]
    }
}

#[cfg(feature = "solution_983")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let days: Vec<i32> = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	let costs: Vec<i32> = serde_json::from_str(&input_values[1]).expect("Failed to parse input");
	json!(Solution::mincost_tickets(days, costs))
}
