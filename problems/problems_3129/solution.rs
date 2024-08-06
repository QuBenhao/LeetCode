use serde_json::{json, Value};

pub struct Solution;

use std::cmp::min;
impl Solution {
    pub fn number_of_stable_arrays(zero: i32, one: i32, limit: i32) -> i32 {
		let mod_num = 1_000_000_007;
		let mut dp = vec![vec![vec![0; 2]; one as usize + 1]; zero as usize + 1];
		for i in 1..=min(zero, limit) as usize {
			dp[i][0][0] = 1;
		}
		for j in 1..=min(one, limit) as usize {
			dp[0][j][1] = 1;
		}
		for i in 1..=zero as usize {
			for j in 1..=one as usize {
				dp[i][j][0] = (dp[i - 1][j][0] + dp[i - 1][j][1]) % mod_num;
				if i as i32 > limit {
					dp[i][j][0] = (dp[i][j][0] - dp[i - limit as usize - 1][j][1] + mod_num) % mod_num;
				}
				dp[i][j][1] = (dp[i][j - 1][0] + dp[i][j - 1][1]) % mod_num;
				if j as i32 > limit {
					dp[i][j][1] = (dp[i][j][1] - dp[i][j - limit as usize - 1][0] + mod_num) % mod_num;
				}
			}
		}
		(dp[zero as usize][one as usize][0] + dp[zero as usize][one as usize][1]) % mod_num
    }
}

#[cfg(feature = "solution_3129")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let zero: i32 = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	let one: i32 = serde_json::from_str(&input_values[1]).expect("Failed to parse input");
	let limit: i32 = serde_json::from_str(&input_values[2]).expect("Failed to parse input");
	json!(Solution::number_of_stable_arrays(zero, one, limit))
}
