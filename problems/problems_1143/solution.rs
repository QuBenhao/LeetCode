use serde_json::{json, Value};

pub struct Solution;

impl Solution {
    pub fn longest_common_subsequence(text1: String, text2: String) -> i32 {
		let m = text1.len();
		let n = text2.len();
		let mut dp: Vec<Vec<i32>> = vec![vec![0; n + 1]; m + 1];
		for i in 1..=m {
			let c1 = text1.chars().nth(i - 1).unwrap();
			for j in 1..=n {
				let c2 = text2.chars().nth(j - 1).unwrap();
				if c1 == c2 {
					dp[i][j] = dp[i - 1][j - 1] + 1;
				} else {
					dp[i][j] = dp[i - 1][j].max(dp[i][j - 1]);
				}
			}
		}
		dp[m][n]
    }
}

#[cfg(feature = "solution_1143")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let text1: String = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	let text2: String = serde_json::from_str(&input_values[1]).expect("Failed to parse input");
	json!(Solution::longest_common_subsequence(text1, text2))
}
