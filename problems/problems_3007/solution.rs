use serde_json::{json, Value};

pub struct Solution;

impl Solution {
    pub fn find_maximum_number(mut k: i64, x: i32) -> i64 {
		let bit_length = |mut n: i64| {
			let mut res = 0;
			while n > 0 {
				n >>= 1;
				res += 1;
			}
			res
		};

		let mut num: i64 = 0;
		let mut pre1: i64 = 0;
		for i in (0..bit_length((k + 1) << x) - 1).rev() {
			let cur = (pre1 << i) + (((i / x) as i64) << i >> 1);
			if cur <= k {
				k -= cur;
				num |= 1 << i;
				if (i + 1) % x == 0 {
					pre1 += 1;
				}
			}
		}
		num - 1
    }
}

#[cfg(feature = "solution_3007")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let k: i64 = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	let x: i32 = serde_json::from_str(&input_values[1]).expect("Failed to parse input");
	json!(Solution::find_maximum_number(k, x))
}
