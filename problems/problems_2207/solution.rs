use serde_json::{json, Value};

pub struct Solution;

impl Solution {
    pub fn maximum_subsequence_count(text: String, pattern: String) -> i64 {
		let mut ans = 0i64;
		let mut p0 = 0i64;
		let mut p1 = 0i64;
		let bytes = pattern.as_bytes();
		for c in text.bytes() {
			if c == bytes[1] {
				p1 += 1;
				ans += p0;
			}
			if c == bytes[0] {
				p0 += 1
			}
		}
		ans + p0.max(p1)
    }
}

#[cfg(feature = "solution_2207")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let text: String = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	let pattern: String = serde_json::from_str(&input_values[1]).expect("Failed to parse input");
	json!(Solution::maximum_subsequence_count(text, pattern))
}
