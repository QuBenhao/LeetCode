#![allow(non_snake_case)]
use serde_json::{json, Value};

pub struct Solution;

struct Trie {
	children: [Option<Box<Trie>>; 26],
	is_end: bool,
}

impl Trie {
	fn new() -> Self {
		Self {
			children: Default::default(),
			is_end: false,
		}
	}

	fn insert(&mut self, word: &str) {
		let mut node = self;
		for c in word.chars() {
			let idx = c as usize - 'a' as usize;
			node = node.children[idx].get_or_insert_with(|| Box::new(Trie::new()));
		}
		node.is_end = true;
	}

	fn search(&self, word: &str) -> String {
		let mut node = self;
		let mut prefix = String::new();
		for c in word.chars() {
			let idx = c as usize - 'a' as usize;
			node = match &node.children[idx] {
				Some(child) => {
					prefix.push(c);
					if child.is_end {
						return prefix;
					}
					child
				}
				None => return word.to_string(),
			};
		}
		word.to_string()
	}
}

impl Solution {
    pub fn replace_words(dictionary: Vec<String>, sentence: String) -> String {
		let mut trie = Trie::new();
		for word in dictionary {
			trie.insert(&word);
		}
		let mut result = String::new();
		for word in sentence.split_whitespace() {
			result.push_str(&trie.search(word));
			result.push(' ');
		}
		result.pop();
		result
    }
}

#[cfg(feature = "solution_LCR_063")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let dictionary: Vec<String> = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	let sentence: String = serde_json::from_str(&input_values[1]).expect("Failed to parse input");
	json!(Solution::replace_words(dictionary, sentence))
}
