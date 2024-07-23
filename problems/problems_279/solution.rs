use serde_json::{json, Value};

pub struct Solution;

use std::collections::HashSet;

impl Solution {
	fn is_divided_by_4(s: &HashSet<i32>, n: i32, count: i32) -> bool {
		if count == 1 {
			return s.contains(&n);
		}
		for i in s.iter() {
			if Solution::is_divided_by_4(s, n - i, count - 1) {
				return true;
			}
		}
		false
	}
    pub fn num_squares(n: i32) -> i32 {
		let mut squares: HashSet<i32> = HashSet::new();
		let mut i: i32 = 1;
		while i * i <= n {
			squares.insert(i * i);
			i += 1;
		}
		for i in 1..n {
			if Solution::is_divided_by_4(&squares, n, i) {
				return i;
			}
		}
		n
    }
}

#[cfg(feature = "solution_279")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let n: i32 = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	json!(Solution::num_squares(n))
}
