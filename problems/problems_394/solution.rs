use serde_json::{json, Value};

pub struct Solution;

impl Solution {
    pub fn decode_string(s: String) -> String {
		let mut stack: Vec<(String, usize)> = vec![];
		let mut num = 0;
		let mut res = String::new();
		for c in s.chars() {
			if c == '[' {
				stack.push((res.clone(), num));
				res = String::new();
				num = 0;
			} else if c == ']' {
				let (last_res, t) = stack.pop().unwrap();
				res = last_res + &*res.repeat(t);
			} else if c.is_digit(10) {
				num = num * 10 + c.to_digit(10).unwrap() as usize;
			} else {
				res.push(c);
			}
		}
		res
    }
}

#[cfg(feature = "solution_394")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let s: String = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	json!(Solution::decode_string(s))
}
