use serde_json::{json, Value};

pub struct Solution;

impl Solution {
    pub fn min_distance(word1: String, word2: String) -> i32 {
		let m: usize = word1.len();
		let n: usize = word2.len();
		let mut dp: Vec<Vec<i32>> = vec![vec![0; n + 1]; m + 1];
		for i in 0..=m {
			dp[i][0] = i as i32;
		}
		for j in 0..=n {
			dp[0][j] = j as i32;
		}
		for i in 1..=m {
			for j in 1..=n {
				if word1.chars().nth(i - 1).unwrap() == word2.chars().nth(j - 1).unwrap() {
					dp[i][j] = dp[i - 1][j - 1];
				} else {
					dp[i][j] = dp[i - 1][j - 1].min(dp[i - 1][j].min(dp[i][j - 1])) + 1;
				}
			}
		}
		dp[m][n]
    }
}

#[cfg(feature = "solution_72")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let word1: String = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	let word2: String = serde_json::from_str(&input_values[1]).expect("Failed to parse input");
	json!(Solution::min_distance(word1, word2))
}
