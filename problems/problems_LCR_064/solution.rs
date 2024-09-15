#![allow(non_snake_case)]
use serde_json::{json, Value};

#[derive(Default)]
struct Trie {
    children: [Option<Box<Trie>>; 26],
    is_end: bool,
}

impl Trie {
    fn new() -> Self {
        Default::default()
    }
}

fn query(node: &Trie, word: &str, index: usize, change: bool) -> bool {
    if index == word.len() {
		return change && node.is_end;
	}
	let c = word.chars().nth(index).unwrap();
	let cur = c as usize - 'a' as usize;
	if let Some(child) = &node.children[cur] {
		if query(child, word, index + 1, change) {
			return true;
		}
	}
	if !change {
		for i in 0..26 {
			if i == cur {
				continue;
			}
			if let Some(child) = &node.children[i] {
				if query(child, word, index + 1, true) {
					return true;
				}
			}
		}
	}
    false
}

struct MagicDictionary {
    trie: Trie,
}


/**
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl MagicDictionary {
    /** Initialize your data structure here. */
    fn new() -> Self {
        Self {
            trie: Trie::new(),
        }
    }

    fn build_dict(&mut self, dictionary: Vec<String>) {
        for word in dictionary {
            let mut node = &mut self.trie;
            for c in word.as_bytes() {
                let c = (c - b'a') as usize;
                node = node.children[c].get_or_insert_with(|| Box::new(Trie::new()));
            }
            node.is_end = true;
        }
    }

    fn search(&self, search_word: String) -> bool {
        query(&self.trie, &search_word, 0, false)
    }
}

/**
 * Your MagicDictionary object will be instantiated and called as such:
 * let obj = MagicDictionary::new();
 * obj.build_dict(dictionary);
 * let ret_2: bool = obj.search(searchWord);
 */

#[cfg(feature = "solution_LCR_064")]
pub fn solve(input_string: String) -> Value {
    let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
    let operators: Vec<String> = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
    let op_values: Vec<Vec<Value>> = serde_json::from_str(&input_values[1]).expect("Failed to parse input");
    let mut obj = MagicDictionary::new();
    let mut ans = vec![None];
    for i in 1..operators.len() {
        match operators[i].as_str() {
            "buildDict" => {
                let dictionary: Vec<String> = serde_json::from_value(op_values[i][0].clone()).expect("Failed to parse input");
                obj.build_dict(dictionary);
                ans.push(None);
            }
            "search" => {
                let search_word: String = serde_json::from_value(op_values[i][0].clone()).expect("Failed to parse input");
                ans.push(Some(obj.search(search_word)));
            }
            _ => ans.push(None),
        }
    }
    json!(ans)
}
