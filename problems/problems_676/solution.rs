use serde_json::{json, Value};

#[derive(Default)]
struct TrieNode {
    children: [Option<Box<TrieNode>>; 26],
    is_end: bool,
}

impl TrieNode {
    fn new() -> Self {
        Default::default()
    }

    fn insert(&mut self, word: &str) {
        let mut node = self;
        for c in word.chars() {
            let idx = c as usize - 'a' as usize;
            node = node.children[idx].get_or_insert_with(|| Box::new(TrieNode::new()));
        }
        node.is_end = true;
    }
}

fn query(node: &TrieNode, word: &str, idx: usize, remain: i32) -> bool {
    if idx == word.len() {
        return remain == 0 && node.is_end;
    }
    let c = word.chars().nth(idx).unwrap();
    let cur = c as usize - 'a' as usize;
    if let Some(child) = &node.children[cur] {
        if query(child, word, idx + 1, remain) {
            return true;
        }
    }
    if remain == 0 {
        return false;
    }
    for i in 0..26 {
        if i == cur {
            continue;
        }
        if let Some(child) = &node.children[i] {
            if query(child, word, idx + 1, remain - 1) {
                return true;
            }
        }
    }
    false
}

struct MagicDictionary {
    root: TrieNode,
}


/**
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl MagicDictionary {
    fn new() -> Self {
        Self {
            root: TrieNode::new(),
        }
    }

    fn build_dict(&mut self, dictionary: Vec<String>) {
        for word in dictionary {
            self.root.insert(&word);
        }
    }

    fn search(&self, search_word: String) -> bool {
        query(&self.root, &search_word, 0, 1)
    }
}

/**
 * Your MagicDictionary object will be instantiated and called as such:
 * let obj = MagicDictionary::new();
 * obj.build_dict(dictionary);
 * let ret_2: bool = obj.search(searchWord);
 */

#[cfg(feature = "solution_676")]
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
			},
			"search" => {
				let search_word: String = serde_json::from_value(op_values[i][0].clone()).expect("Failed to parse input");
				ans.push(Some(obj.search(search_word)));
			},
			_ => ans.push(None),
		}
	}
	json!(ans)
}
