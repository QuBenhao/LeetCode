#![allow(non_snake_case)]
use serde_json::{json, Value};

pub struct Solution;

impl Solution {
    pub fn add_binary(a: String, b: String) -> String {
		if a.len() < b.len() {
			return Solution::add_binary(b, a);
		}
		let mut res: Vec<char> = Vec::new();
		let mut carry = 0;
		let n = a.len();
		let d = n - b.len();
		let chars_a: Vec<char> = a.chars().collect();
		let chars_b: Vec<char> = b.chars().collect();
		for i in (0..n).rev() {
			let mut sum = carry;
			if i >= d {
				if chars_b[i - d] == '1' {
					sum += 1;
				}
			}
			if chars_a[i] == '1' {
				sum += 1;
			}
			carry = sum / 2;
			res.push(std::char::from_digit(sum % 2, 10).unwrap());
		}
		if carry > 0 {
			res.push('1');
		}
		res.iter().rev().collect()
    }
}

#[cfg(feature = "solution_LCR_002")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let a: String = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	let b: String = serde_json::from_str(&input_values[1]).expect("Failed to parse input");
	json!(Solution::add_binary(a, b))
}
