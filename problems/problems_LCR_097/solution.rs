#![allow(non_snake_case)]
use serde_json::{json, Value};

pub struct Solution;

impl Solution {
    pub fn num_distinct(s: String, t: String) -> i32 {
        let t = t.chars().collect::<Vec<_>>();
        let mut dp = vec![0i64; t.len() + 1];
        dp[0] = 1i64;
        for c in s.chars() {
            for i in (1..=t.len()).rev() {
                if c == t[i - 1] {
                    dp[i] = dp[i].checked_add(dp[i - 1]).unwrap_or(0);
                }
            }
        }
        dp[t.len()] as i32
    }
}

#[cfg(feature = "solution_LCR_097")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let s: String = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	let t: String = serde_json::from_str(&input_values[1]).expect("Failed to parse input");
	json!(Solution::num_distinct(s, t))
}
