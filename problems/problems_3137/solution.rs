use serde_json::{json, Value};

pub struct Solution;
use std::collections::HashMap;
impl Solution {
    pub fn minimum_operations_to_make_k_periodic(word: String, k: i32) -> i32 {
		let n: usize = word.len();
		let mut count: HashMap<String, i32> = HashMap::new();
		let mut ans: i32 = 0;
		for i in (0..n).step_by(k as usize) {
			let sub = &word[i..i+k as usize];
			*count.entry(sub.to_string()).or_insert(0) += 1;
			ans = ans.max(count[&sub.to_string()]);
		}
		n as i32 / k - ans
    }
}

#[cfg(feature = "solution_3137")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let word: String = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	let k: i32 = serde_json::from_str(&input_values[1]).expect("Failed to parse input");
	json!(Solution::minimum_operations_to_make_k_periodic(word, k))
}
