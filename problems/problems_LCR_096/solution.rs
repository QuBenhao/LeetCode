#![allow(non_snake_case)]
use serde_json::{json, Value};

pub struct Solution;

impl Solution {
    pub fn is_interleave(s1: String, s2: String, s3: String) -> bool {
		let m = s1.len();
		let n = s2.len();
		if m + n != s3.len() {
			return false;
		}
		let mut dp: Vec<bool> = vec![false; n + 1];
		dp[0] = true;
		for i in 0..=m {
			for j in 0..=n {
				if i > 0 {
					dp[j] = dp[j] && s1.chars().nth(i - 1).unwrap() == s3.chars().nth(i + j - 1).unwrap();
				}
				if j > 0 {
					dp[j] = dp[j] || dp[j - 1] && s2.chars().nth(j - 1).unwrap() == s3.chars().nth(i + j - 1).unwrap();
				}
			}
		}
		dp[n]
    }
}

#[cfg(feature = "solution_LCR_096")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let s1: String = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	let s2: String = serde_json::from_str(&input_values[1]).expect("Failed to parse input");
	let s3: String = serde_json::from_str(&input_values[2]).expect("Failed to parse input");
	json!(Solution::is_interleave(s1, s2, s3))
}
