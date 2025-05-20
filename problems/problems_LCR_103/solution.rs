#![allow(non_snake_case)]
use serde_json::{json, Value};

pub struct Solution;

impl Solution {
    pub fn coin_change(coins: Vec<i32>, amount: i32) -> i32 {

    }
}

#[cfg(feature = "solution_LCR_103")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let coins: Vec<i32> = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	let amount: i32 = serde_json::from_str(&input_values[1]).expect("Failed to parse input");
	json!(Solution::coin_change(coins, amount))
}
