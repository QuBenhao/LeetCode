use serde_json::{json, Value};

pub struct Solution;

use std::collections::hash_set;
impl Solution {
    pub fn dest_city(paths: Vec<Vec<String>>) -> String {
		let mut cities: hash_set::HashSet<String> = hash_set::HashSet::new();
		for path in paths.iter() {
			cities.insert(path[0].clone());
		}
		for path in paths.iter() {
			if !cities.contains(&path[1]) {
				return path[1].clone();
			}
		}
		"".to_string()
    }
}

#[cfg(feature = "solution_1436")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let paths: Vec<Vec<String>> = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	json!(Solution::dest_city(paths))
}
