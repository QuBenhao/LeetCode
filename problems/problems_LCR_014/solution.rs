#![allow(non_snake_case)]
use serde_json::{json, Value};

pub struct Solution;

impl Solution {
    pub fn check_inclusion(s1: String, s2: String) -> bool {
		let mut count: [i32; 26] = [0; 26];
		let s1: Vec<char> = s1.chars().collect();
		let s2: Vec<char> = s2.chars().collect();
		for c in s1.iter() {
			count[(*c as u8 - b'a') as usize] += 1;
		}
		for i in 0..s2.len() {
			count[(s2[i] as u8 - b'a') as usize] -= 1;
			if i >= s1.len() {
				count[(s2[i - s1.len()] as u8 - b'a') as usize] += 1;
			}
			if i >= s1.len() - 1 && count.iter().all(|&x| x == 0) {
				return true;
			}
		}
		false
    }
}

#[cfg(feature = "solution_LCR_014")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let s1: String = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	let s2: String = serde_json::from_str(&input_values[1]).expect("Failed to parse input");
	json!(Solution::check_inclusion(s1, s2))
}
