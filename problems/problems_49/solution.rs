use serde_json::{json, Value};

pub struct Solution;

use std::collections::HashMap;
impl Solution {
    pub fn group_anagrams(strs: Vec<String>) -> Vec<Vec<String>> {
		let mut map: HashMap<String, Vec<String>> = HashMap::new();
		for s in strs {
			let mut key: Vec<char> = s.chars().collect();
			key.sort();
			let key_str: String = key.iter().collect();
			map.entry(key_str).or_insert(Vec::new()).push(s);
		}
		map.into_iter().map(|(_, v)| v).collect()
    }
}

#[cfg(feature = "solution_49")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let strs: Vec<String> = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	json!(Solution::group_anagrams(strs))
}
