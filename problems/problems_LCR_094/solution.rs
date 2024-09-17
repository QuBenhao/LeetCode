#![allow(non_snake_case)]
use serde_json::{json, Value};

pub struct Solution;

impl Solution {
    pub fn min_cut(s: String) -> i32 {
		let n = s.len();
		let s = s.chars().collect::<Vec<char>>();
		let mut dp = vec![vec![false; n]; n];
		for i in (0..n).rev() {
			for j in i..n {
				dp[i][j] = s[i] == s[j] && (j - i < 2 || dp[i + 1][j - 1]);
			}
		}
		let mut cut = vec![n as i32; n + 1];
		cut[0] = -1;
		for i in 0..n {
			for j in 0..=i {
				if dp[j][i] {
					cut[i + 1] = cut[i + 1].min(cut[j] + 1);
				}
			}
		}
		cut[n]
    }
}

#[cfg(feature = "solution_LCR_094")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let s: String = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	json!(Solution::min_cut(s))
}
