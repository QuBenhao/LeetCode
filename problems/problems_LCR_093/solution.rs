#![allow(non_snake_case)]
use serde_json::{json, Value};

pub struct Solution;

impl Solution {
    pub fn len_longest_fib_subseq(arr: Vec<i32>) -> i32 {
		let mut ans = 0;
		let mut index = std::collections::HashMap::new();
		let n = arr.len();
		for i in 0..n {
			index.insert(arr[i], i);
		}
		let mut dp = vec![vec![2; n]; n];
		for i in 0..n {
			for j in 0..i {
				let k = index.get(&(arr[i] - arr[j]));
				if k.is_some() && k.unwrap() < &j {
					dp[i][j] = dp[j][*k.unwrap()] + 1;
					ans = ans.max(dp[i][j]);
				}
			}
		}
		ans
    }
}

#[cfg(feature = "solution_LCR_093")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let arr: Vec<i32> = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	json!(Solution::len_longest_fib_subseq(arr))
}
