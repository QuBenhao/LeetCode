#![allow(non_snake_case)]
use serde_json::{json, Value};

pub struct Solution;

impl Solution {
    pub fn min_flips_mono_incr(s: String) -> i32 {
		let n = s.len() as i32;
		let mut ans = n;
		let mut one = 0;
		let chars: Vec<char> = s.chars().collect();
		for i in 0..n {
			ans = ans.min(one * 2 - i);
			if chars[i as usize] == '1' {
				one += 1;
			}
		}
		one.min(ans + n - one)
    }
}

#[cfg(feature = "solution_LCR_092")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let s: String = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	json!(Solution::min_flips_mono_incr(s))
}
