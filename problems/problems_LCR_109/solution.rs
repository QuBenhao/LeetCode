#![allow(non_snake_case)]
use serde_json::{json, Value};

pub struct Solution;
use std::collections::{HashSet, VecDeque};
impl Solution {
    pub fn open_lock(deadends: Vec<String>, target: String) -> i32 {
		let deadends_set = deadends.iter().collect::<HashSet<_>>();
		let mut visited = HashSet::new();
		let mut queue = VecDeque::new();
		queue.push_back(("0000".to_string(), 0));
		while !queue.is_empty() {
			let (current, steps) = queue.pop_front().unwrap();
			if deadends_set.contains(&current) {
				continue;
			}
			if current == target {
				return steps;
			}
			if visited.contains(&current) {
				continue;
			}
			visited.insert(current.clone());
			for i in 0..4 {
				let mut next = current.clone().into_bytes();
				let next_char = next[i] as char;
				next[i] = ((next_char as u8 - b'0' + 1) % 10 + b'0') as u8;
				queue.push_back((String::from_utf8(next.clone()).unwrap(), steps + 1));
				next[i] = ((next_char as u8 - b'0' + 9) % 10 + b'0') as u8;
				queue.push_back((String::from_utf8(next).unwrap(), steps + 1));
			}
		}
		-1
    }
}

#[cfg(feature = "solution_LCR_109")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let deadends: Vec<String> = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	let target: String = serde_json::from_str(&input_values[1]).expect("Failed to parse input");
	json!(Solution::open_lock(deadends, target))
}
