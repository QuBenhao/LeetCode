use serde_json::{json, Value};

pub struct Solution;

impl Solution {
    pub fn minimum_operations(num: String) -> i32 {
		let n: i32 = num.len() as i32;
		let mut zero: bool = false;
		let mut five: bool = false;
		let mut idx = n - 1;
		while idx >= 0 {
			let c: char = num.chars().nth(idx as usize).unwrap();
			if zero && (c == '0' || c == '5') || five && (c == '2' || c == '7') {
				return n - idx - 2;
			}
			if c == '0' {
				zero = true;
			} else if c == '5' {
				five = true;
			}
			idx -= 1;
		}
		if zero {
			n - 1
		} else {
			n
		}
    }
}

#[cfg(feature = "solution_2844")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let num: String = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	json!(Solution::minimum_operations(num))
}
