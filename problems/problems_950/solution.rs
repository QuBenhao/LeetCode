use serde_json::{json, Value};

pub struct Solution;

use std::collections::VecDeque;
impl Solution {
    pub fn deck_revealed_increasing(deck: Vec<i32>) -> Vec<i32> {
		let mut q: VecDeque<i32> = VecDeque::new();
		let mut deck = deck;
		deck.sort_unstable();
		for i in (0..deck.len()).rev() {
			if !q.is_empty() {
				let last = q.pop_back().unwrap();
				q.push_front(last);
			}
			q.push_front(deck[i]);
		}
		q.into_iter().collect()
    }
}

#[cfg(feature = "solution_950")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let deck: Vec<i32> = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	json!(Solution::deck_revealed_increasing(deck))
}
