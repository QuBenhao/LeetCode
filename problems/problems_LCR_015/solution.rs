#![allow(non_snake_case)]
use serde_json::{json, Value};

pub struct Solution;

impl Solution {
    pub fn find_anagrams(s: String, p: String) -> Vec<i32> {
		let length = p.len();
		let mut count: Vec<i32> = vec![0; 26];
		let mut diff: i32 = 0;
		for c in p.chars() {
			let idx = (c as u32 - 'a' as u32) as usize;
			count[idx] += 1;
			if count[idx] == 1 {
				diff += 1;
			}
		}
		let mut ans: Vec<i32> = Vec::new();
		for (i, c) in s.chars().enumerate() {
			let idx = (c as u32 - 'a' as u32) as usize;
			count[idx] -= 1;
			if count[idx] == 0 {
				diff -= 1;
			} else if count[idx] == -1 {
				diff += 1;
			}
			if i + 1 >= length {
				if diff == 0 {
					ans.push((i + 1 - length) as i32);
				}
				let old = (s.chars().nth(i + 1 - length).unwrap() as u32 - 'a' as u32) as usize;
				count[old] += 1;
				if count[old] == 0 {
					diff -= 1;
				} else if count[old] == 1 {
					diff += 1;
				}
			}
		}
		ans
    }
}

#[cfg(feature = "solution_LCR_015")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let s: String = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	let p: String = serde_json::from_str(&input_values[1]).expect("Failed to parse input");
	json!(Solution::find_anagrams(s, p))
}
