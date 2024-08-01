use serde_json::{json, Value};

pub struct Solution;

impl Solution {
    pub fn coin_change(coins: Vec<i32>, amount: i32) -> i32 {
		if amount == 0 {
			return 0;
		}
		let mut dp: Vec<i32> = vec![amount + 1; (amount + 1) as usize];
		dp[0] = 0;
		for i in 1..=amount {
			for &coin in coins.iter() {
				if i >= coin {
					dp[i as usize] = dp[i as usize].min(dp[(i - coin) as usize] + 1);
				}
			}
		}
		if dp[amount as usize] == amount + 1 {
			return -1;
		}
		dp[amount as usize]
    }
}

#[cfg(feature = "solution_322")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let coins: Vec<i32> = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	let amount: i32 = serde_json::from_str(&input_values[1]).expect("Failed to parse input");
	json!(Solution::coin_change(coins, amount))
}
