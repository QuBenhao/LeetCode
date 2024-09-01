use serde_json::{json, Value};

pub struct Solution;

impl Solution {
    pub fn can_partition(nums: Vec<i32>) -> bool {
		let mut s: i32 = 0;
		for num in &nums {
			s += num;
		}
		if s % 2 != 0 {
			return false;
		}
		let s = s / 2;
		let mut dp = vec![false; (s + 1) as usize];
		dp[0] = true;
		for num in &nums {
			for i in (*num..=s).rev() {
				dp[i as usize] = dp[i as usize] || dp[(i - num) as usize];
			}
		}
		dp[s as usize]
    }
}

#[cfg(feature = "solution_416")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let nums: Vec<i32> = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	json!(Solution::can_partition(nums))
}
