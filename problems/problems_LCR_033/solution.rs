#![allow(non_snake_case)]
use serde_json::{json, Value};

pub struct Solution;
use std::collections::HashMap;
impl Solution {
    pub fn group_anagrams(strs: Vec<String>) -> Vec<Vec<String>> {
		let mut map: HashMap<Vec<u8>, Vec<String>> = HashMap::new();
		for s in strs {
			let mut cnt = vec![0; 26];
			for c in s.bytes() {
				cnt[(c - b'a') as usize] += 1;
			}
			map.entry(cnt).or_insert(vec![]).push(s);
		}
		map.into_iter().map(|(_, v)| v).collect()
    }
}

#[cfg(feature = "solution_LCR_033")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let strs: Vec<String> = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	json!(Solution::group_anagrams(strs))
}
