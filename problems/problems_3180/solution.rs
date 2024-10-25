use serde_json::{json, Value};

pub struct Solution;

impl Solution {
    pub fn max_total_reward(reward_values: Vec<i32>) -> i32 {
        let mut reward_values = reward_values.clone();
        reward_values.sort();
        let m = reward_values[reward_values.len() - 1] as usize;
        let mut dp = vec![0; 2 * m];
        dp[0] = 1;

        for &x in &reward_values {
            let x = x as usize;
            for k in (x..2 * x).rev() {
                if dp[k - x] == 1 {
                    dp[k] = 1;
                }
            }
        }

        let mut res = 0;
        for (i, &value) in dp.iter().enumerate() {
            if value == 1 {
                res = i;
            }
        }
        res as i32
    }
}


#[cfg(feature = "solution_3180")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let reward_values: Vec<i32> = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	json!(Solution::max_total_reward(reward_values))
}
