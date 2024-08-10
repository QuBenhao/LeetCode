use serde_json::{json, Value};

pub struct Solution;

use std::collections::HashSet;
impl Solution {
    pub fn word_break(s: String, word_dict: Vec<String>) -> bool {
		let mut words: HashSet<String> = HashSet::new();
		for word in word_dict {
			words.insert(word);
		}
		let n = s.len();
		let mut dp: Vec<bool> = vec![false; n + 1];
		dp[0] = true;
		for i in 1..=n {
			for j in 0..i {
				if dp[j] && words.contains(&s[j..i].to_string()) {
					dp[i] = true;
					break;
				}
			}
		}
		dp[n]
    }
}

#[cfg(feature = "solution_139")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let s: String = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	let word_dict: Vec<String> = serde_json::from_str(&input_values[1]).expect("Failed to parse input");
	json!(Solution::word_break(s, word_dict))
}
