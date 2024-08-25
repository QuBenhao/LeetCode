#![allow(non_snake_case)]
use serde_json::{json, Value};

pub struct Solution;

impl Solution {
    pub fn divide(a: i32, b: i32) -> i32 {
		if a == i32::MIN && b == -1 {
			return i32::MAX;
		}
		let mut dividend: u32 = a.unsigned_abs();
		let divisor: u32 = b.unsigned_abs();
		let mut ans: u32 = 0;
		for i in (0u32..32).rev() {
			if (dividend >> i) >= divisor {
				ans |= 1 << i;
				dividend -= divisor << i;
			}
		}
		if (a > 0) == (b > 0) {
			ans as i32
		} else {
			if ans == i32::MIN.unsigned_abs() {
				i32::MIN
			} else {
				-(ans as i32)
			}
		}
    }
}

#[cfg(feature = "solution_LCR_001")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let a: i32 = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	let b: i32 = serde_json::from_str(&input_values[1]).expect("Failed to parse input");
	json!(Solution::divide(a, b))
}
