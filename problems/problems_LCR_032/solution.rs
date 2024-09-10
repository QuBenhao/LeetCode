#![allow(non_snake_case)]
use serde_json::{json, Value};

pub struct Solution;

impl Solution {
    pub fn is_anagram(s: String, t: String) -> bool {
		if s.len() != t.len() || s == t {
			return false;
		}
		let mut cnt: [i32; 26] = [0; 26];
		let chars_s: Vec<char> = s.chars().collect();
		let chars_t: Vec<char> = t.chars().collect();
		for i in 0..s.len() {
			cnt[(chars_s[i] as u8 - b'a') as usize] += 1;
			cnt[(chars_t[i] as u8 - b'a') as usize] -= 1;
		}
		for i in 0..26 {
			if cnt[i] != 0 {
				return false;
			}
		}
		true
    }
}

#[cfg(feature = "solution_LCR_032")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let s: String = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	let t: String = serde_json::from_str(&input_values[1]).expect("Failed to parse input");
	json!(Solution::is_anagram(s, t))
}
