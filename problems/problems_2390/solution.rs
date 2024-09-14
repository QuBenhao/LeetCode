use serde_json::{json, Value};

pub struct Solution;

impl Solution {
    pub fn remove_stars(s: String) -> String {
		let mut str = String::new();
		let chars: Vec<char> = s.chars().collect();
		for i in 0..s.len() {
			if chars[i] == '*' {
				if !str.is_empty() {
					str.pop();
				}
			} else {
				str.push(chars[i]);
			}
		}
		str
    }
}

#[cfg(feature = "solution_2390")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let s: String = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	json!(Solution::remove_stars(s))
}
