#![allow(non_snake_case)]
use serde_json::{json, Value};

pub struct Solution;

impl Solution {
    pub fn ladder_length(begin_word: String, end_word: String, word_list: Vec<String>) -> i32 {
		use std::collections::{HashSet, VecDeque};
		let mut word_set: HashSet<String> = HashSet::new();
		for word in word_list.iter() {
			word_set.insert(word.clone());
		}
		if !word_set.contains(&end_word) {
			return 0;
		}
		let mut queue: VecDeque<String> = VecDeque::new();
		queue.push_back(begin_word.clone());
		let mut visited: HashSet<String> = HashSet::new();
		visited.insert(begin_word);
		let mut level: i32 = 1;
		while !queue.is_empty() {
			let mut size: usize = queue.len();
			while size > 0 {
				let current_word: String = queue.pop_front().unwrap();
				let mut chars: Vec<char> = current_word.chars().collect();
				for i in 0..chars.len() {
					let old_char: char = chars[i];
					for c in 'a'..='z' {
						chars[i] = c;
						let new_word: String = chars.iter().collect();
						if word_set.contains(&new_word) {
							if new_word == end_word {
								return level + 1;
							}
							if !visited.contains(&new_word) {
								visited.insert(new_word.clone());
								queue.push_back(new_word);
							}
						}
					}
					chars[i] = old_char;
				}
				size -= 1;
			}
			level += 1;
		}
		0
    }
}

#[cfg(feature = "solution_LCR_108")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let begin_word: String = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	let end_word: String = serde_json::from_str(&input_values[1]).expect("Failed to parse input");
	let word_list: Vec<String> = serde_json::from_str(&input_values[2]).expect("Failed to parse input");
	json!(Solution::ladder_length(begin_word, end_word, word_list))
}
