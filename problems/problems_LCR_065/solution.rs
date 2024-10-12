#![allow(non_snake_case)]
use serde_json::{json, Value};

pub struct Solution;

impl Solution {
    pub fn minimum_length_encoding(words: Vec<String>) -> i32 {
		let mut reversed_words: Vec<String> = words.iter().map(|x| x.chars().rev().collect()).collect();
		reversed_words.sort();
		let mut ans: i32 = 0;
		for i in 0..reversed_words.len() {
			if i == reversed_words.len() - 1 || !reversed_words[i + 1].starts_with(&reversed_words[i]) {
				ans += reversed_words[i].len() as i32 + 1;
			}
		}
		ans
    }
}

#[cfg(feature = "solution_LCR_065")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let words: Vec<String> = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	json!(Solution::minimum_length_encoding(words))
}
