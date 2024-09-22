use serde_json::{json, Value};

pub struct Solution;

impl Solution {
    pub fn max_score_sightseeing_pair(values: Vec<i32>) -> i32 {
		let mut ans = 0;
		let mut left = values[0];
		let n = values.len();
		for i in 1..n {
			ans = ans.max(left + values[i] - i as i32);
			left = left.max(values[i] + i as i32);
		}
		ans
    }
}

#[cfg(feature = "solution_1014")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let values: Vec<i32> = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	json!(Solution::max_score_sightseeing_pair(values))
}
