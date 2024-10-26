use serde_json::{json, Value};

pub struct Solution;

impl Solution {
    pub fn max_total_reward(reward_values: Vec<i32>) -> i32 {
        let mut reward_values = reward_values;
        reward_values.sort_unstable();
        reward_values.dedup();
        let max = reward_values.iter().fold(0, |acc, &x| acc.max(x));
        let mut dp = vec![false; 2 * max as usize + 1];
        dp[0] = true;
        unsafe {
            for v in reward_values.into_iter() {
                for x in (v..v << 1).rev() {
                    *(dp.get_unchecked_mut(x as usize)) |= *dp.get_unchecked((x - v) as usize);
                }
            }
        }
        dp.iter().enumerate().rfind(|(_, &x)| x).unwrap().0 as i32
    }
}

#[cfg(feature = "solution_3181")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let reward_values: Vec<i32> = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	json!(Solution::max_total_reward(reward_values))
}
