use serde_json::{json, Value};

pub struct Solution;

impl Solution {
    pub fn find_integers(n: i32) -> i32 {
		let mut dp: Vec<i32> = vec![0; 31];
		dp[0] = 1;
		dp[1] = 2;
		for i in 2..31 {
			dp[i] = dp[i - 1] + dp[i - 2];
		}
		let num = n + 1;
		let mut ans: i32 = 0;
		let mut pre: i32 = 0;
		for i in (0..30).rev() {
			let val = 1 << i;
			if (num & val) != 0 {
				ans += dp[i];
				if pre == 1 {
					break;
				}
				pre = 1;
			} else {
				pre = 0;
			}
		}
		ans
    }
}

#[cfg(feature = "solution_600")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let n: i32 = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	json!(Solution::find_integers(n))
}
