use serde_json::{json, Value};

pub struct Solution;

impl Solution {
    pub fn min_end(n: i32, x: i32) -> i64 {
		let mut n = n;
		n -= 1;
		let mut x: i64 = x as i64;
		let mut i: i64 = 0;
		let mut j: i32 = 0;
		while n >> j > 0 {
			if ((x >> i) & 1) == 0 {
				x |= ((n >> j & 1) as i64) << i;
				j += 1;
			}
			i += 1;
		}
		x
    }
}

#[cfg(feature = "solution_3133")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let n: i32 = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	let x: i32 = serde_json::from_str(&input_values[1]).expect("Failed to parse input");
	json!(Solution::min_end(n, x))
}
