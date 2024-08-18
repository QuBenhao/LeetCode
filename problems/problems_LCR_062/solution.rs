#![allow(non_snake_case)]
use serde_json::{json, Value};


use std::collections::HashMap;
struct Trie {
	children: HashMap<char, Trie>,
	is_end: bool
}


/**
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl Trie {

    /** Initialize your data structure here. */
    fn new() -> Self {
		Trie{
			children: HashMap::new(),
			is_end: false
		}
    }
    
    /** Inserts a word into the trie. */
    fn insert(&mut self, word: String) {
		let mut node = self;
		for c in word.chars() {
			node = node.children.entry(c).or_insert(Trie::new());
		}
		node.is_end = true;
    }

	fn search_node(&self, word: String) -> Option<&Trie> {
		let mut node = self;
		for c in word.chars() {
			if let Some(next_node) = node.children.get(&c) {
				node = next_node;
			} else {
				return None;
			}
		}
		Some(node)
	}
    
    /** Returns if the word is in the trie. */
    fn search(&self, word: String) -> bool {
		let node = self.search_node(word);
		node.is_some_and(|node| node.is_end)
    }
    
    /** Returns if there is any word in the trie that starts with the given prefix. */
    fn starts_with(&self, prefix: String) -> bool {
		self.search_node(prefix).is_some()
    }
}

/**
 * Your Trie object will be instantiated and called as such:
 * let obj = Trie::new();
 * obj.insert(word);
 * let ret_2: bool = obj.search(word);
 * let ret_3: bool = obj.starts_with(prefix);
 */

#[cfg(feature = "solution_LCR_062")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let operators: Vec<String> = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	let op_values: Vec<Vec<Value>> = serde_json::from_str(&input_values[1]).expect("Failed to parse input");
	let mut obj = Trie::new();
	let mut ans = vec![None];
	for i in 1..operators.len() {
		match operators[i].as_str() {
			"insert" => {
				let word: String = serde_json::from_value(op_values[i][0].clone()).expect("Failed to parse input");
				obj.insert(word);
				ans.push(None);
			},
			"search" => {
				let word: String = serde_json::from_value(op_values[i][0].clone()).expect("Failed to parse input");
				ans.push(Some(obj.search(word)));
			},
			"startsWith" => {
				let prefix: String = serde_json::from_value(op_values[i][0].clone()).expect("Failed to parse input");
				ans.push(Some(obj.starts_with(prefix)));
			},
			_ => ans.push(None),
		}
	}
	json!(ans)
}
