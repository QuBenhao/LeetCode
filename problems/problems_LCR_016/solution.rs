#![allow(non_snake_case)]
use serde_json::{json, Value};

pub struct Solution;
use std::collections::HashMap;
use std::cmp::max;
impl Solution {
    pub fn length_of_longest_substring(s: String) -> i32 {
		let mut ans: i32 = 0;
		let mut left: usize = 0;
		let mut map: HashMap<char, usize> = HashMap::new();
		let s: Vec<char> = s.chars().collect();
		for right in 0..s.len() {
			while map.contains_key(&s[right]) {
				map.remove(&s[left]);
				left += 1;
			}
			map.insert(s[right], right);
			ans = max(ans, (right - left + 1) as i32);
		}
		ans
    }
}

#[cfg(feature = "solution_LCR_016")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let s: String = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	json!(Solution::length_of_longest_substring(s))
}
