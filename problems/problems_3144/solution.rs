use serde_json::{json, Value};

pub struct Solution;

impl Solution {
    pub fn minimum_substrings_in_partition(s: String) -> i32 {
		let n = s.len();
		let mut dp = vec![n; n + 1];
		dp[0] = 0;
		let chars: Vec<char> = s.chars().collect();
		for i in 0..n {
			let mut cnt = vec![0; 26];
			let mut max_cnt = 0;
			let mut count = 0;
			for j in (0..=i).rev() {
				let c = chars[j] as usize - 'a' as usize;
				cnt[c] += 1;
				max_cnt = max_cnt.max(cnt[c]);
				if cnt[c] == 1 {
					count += 1;
				}
				if i - j + 1 == max_cnt * count {
					dp[i + 1] = dp[i + 1].min(dp[j] + 1);
				}
			}
		}
		dp[n] as _
    }
}

#[cfg(feature = "solution_3144")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let s: String = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	json!(Solution::minimum_substrings_in_partition(s))
}
