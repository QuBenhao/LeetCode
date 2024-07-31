use serde_json::{json, Value};

pub struct Solution;

impl Solution {
    pub fn maxmium_score(cards: Vec<i32>, cnt: i32) -> i32 {

    }
}

#[cfg(feature = "solution_LCP_40")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let cards: Vec<i32> = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	let cnt: i32 = serde_json::from_str(&input_values[1]).expect("Failed to parse input");
	json!(Solution::maxmium_score(cards, cnt))
}
