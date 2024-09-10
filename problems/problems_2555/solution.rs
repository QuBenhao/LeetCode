use serde_json::{json, Value};

pub struct Solution;

impl Solution {
    pub fn maximize_win(prize_positions: Vec<i32>, k: i32) -> i32 {
		let mut ans: i32 = 0;
		let n = prize_positions.len();
		let mut dp: Vec<i32> = vec![0; n + 1];
		let mut left: usize = 0;
		for (right, &p) in prize_positions.iter().enumerate() {
			while p - prize_positions[left] > k {
				left += 1;
			}
			dp[right + 1] = dp[right].max((right + 1 - left) as i32);
			ans = ans.max(dp[left] + (right + 1 - left) as i32);
		}
		ans
    }
}

#[cfg(feature = "solution_2555")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let prize_positions: Vec<i32> = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	let k: i32 = serde_json::from_str(&input_values[1]).expect("Failed to parse input");
	json!(Solution::maximize_win(prize_positions, k))
}
