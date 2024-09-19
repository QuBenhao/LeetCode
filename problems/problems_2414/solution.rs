use serde_json::{json, Value};

pub struct Solution;

impl Solution {
    pub fn longest_continuous_substring(s: String) -> i32 {
		let mut ans = 1;
		let mut cur = 1;
		let chars = s.chars().collect::<Vec<char>>();
		for i in 0..s.len()-1 {
			if chars[i] as u8 + 1 == chars[i+1] as u8 {
				cur += 1;
				ans = ans.max(cur);
			} else {
				cur = 1;
			}
		}
		ans
    }
}

#[cfg(feature = "solution_2414")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let s: String = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	json!(Solution::longest_continuous_substring(s))
}
