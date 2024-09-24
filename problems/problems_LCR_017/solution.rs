#![allow(non_snake_case)]
use serde_json::{json, Value};

pub struct Solution;
use std::collections::HashMap;
impl Solution {
    pub fn min_window(s: String, t: String) -> String {
		let n = s.len();
		let mut ans_left = 0usize;
		let mut ans_right = 0usize;
		let mut left = 0usize;
		let mut right = 0usize;
		let mut counter: HashMap<u8, i32> = HashMap::new();
		for c in t.bytes() {
			*counter.entry(c).or_insert(0) += 1;
		}
		let mut diff = counter.len() as i32;
		let bytes = s.as_bytes();
		while right < n {
			let c = bytes[right];
			if let Some(x) = counter.get_mut(&c) {
				*x -= 1;
				if *x == 0 {
					diff -= 1;
				}
			}
			right += 1;
			while diff == 0 {
				if right - left < ans_right - ans_left || ans_right == 0 {
					ans_left = left;
					ans_right = right;
				}
				let c = bytes[left];
				if let Some(x) = counter.get_mut(&c) {
					*x += 1;
					if *x == 1 {
						diff += 1;
					}
				}
				left += 1;
			}
		}
		if ans_right == 0 {
			return "".to_string();
		}
		s[ans_left..ans_right].to_string()
    }
}

#[cfg(feature = "solution_LCR_017")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let s: String = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	let t: String = serde_json::from_str(&input_values[1]).expect("Failed to parse input");
	json!(Solution::min_window(s, t))
}
