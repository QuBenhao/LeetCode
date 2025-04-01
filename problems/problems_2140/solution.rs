use serde_json::{json, Value};

pub struct Solution;

impl Solution {
    pub fn most_points(questions: Vec<Vec<i32>>) -> i64 {
		use std::cmp::{max, min};
        let n = questions.len();
		let mut dp = vec![0i64; n + 1];
		for i in 0..n {
			let (points, brainpower) = (questions[i][0], questions[i][1]);
			dp[i + 1] = max(dp[i + 1], dp[i]);
			let next = min(i + brainpower as usize + 1, n);
			dp[next] = max(dp[next], dp[i] + points as i64);
		}
		dp[n]
    }
}

#[cfg(feature = "solution_2140")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let questions: Vec<Vec<i32>> = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	json!(Solution::most_points(questions))
}
