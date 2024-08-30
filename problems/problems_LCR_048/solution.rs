#![allow(non_snake_case)]
use library::lib::tree_node::{TreeNode, tree_to_array, array_to_tree};
use serde_json::{json, Value};


// Definition for a binary tree node.
// #[derive(Debug, PartialEq, Eq)]
// pub struct TreeNode {
//   pub val: i32,
//   pub left: Option<Rc<RefCell<TreeNode>>>,
//   pub right: Option<Rc<RefCell<TreeNode>>>,
// }
// 
// impl TreeNode {
//   #[inline]
//   pub fn new(val: i32) -> Self {
//     TreeNode {
//       val,
//       left: None,
//       right: None
//     }
//   }
// }
use std::rc::Rc;
use std::cell::RefCell;
struct Codec {
	
}

/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl Codec {
    fn new() -> Self {
        Codec{}
    }

    fn serialize(&self, root: Option<Rc<RefCell<TreeNode>>>) -> String {
        if let Some(root) = root {
			let mut ans: Vec<String> = Vec::new();
			fn dfs(node: Option<Rc<RefCell<TreeNode>>>, ans: &mut Vec<String>) {
				if let Some(node) = node {
					let node = node.borrow();
					ans.push(node.val.to_string());
					dfs(node.left.clone(), ans);
					dfs(node.right.clone(), ans);
				} else {
					ans.push("#".to_string());
				}
			}
			dfs(Some(root), &mut ans);
			ans.join(",")
		} else {
			"".to_string()
		}
    }
	
    fn deserialize(&self, data: String) -> Option<Rc<RefCell<TreeNode>>> {
		if data.is_empty() {
			return None;
		}
		let data: Vec<&str> = data.split(",").collect();
		fn dfs(data: &Vec<&str>, idx: &mut usize) -> Option<Rc<RefCell<TreeNode>>> {
			if *idx >= data.len() || data[*idx] == "#" {
				*idx += 1;
				return None;
			}
			let val: i32 = data[*idx].parse().unwrap();
			*idx += 1;
			let left = dfs(data, idx);
			let right = dfs(data, idx);
			let node = Rc::new(RefCell::new(TreeNode::new(val)));
			node.borrow_mut().left = left;
			node.borrow_mut().right = right;
			Some(node)
		}
		let mut idx: usize = 0;
		dfs(&data, &mut idx)
    }
}

/**
 * Your Codec object will be instantiated and called as such:
 * let obj = Codec::new();
 * let data: String = obj.serialize(strs);
 * let ans: Option<Rc<RefCell<TreeNode>>> = obj.deserialize(data);
 */

#[cfg(feature = "solution_LCR_048")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let input_vec0: Vec<Option<i32>> = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	let root: Option<Rc<RefCell<TreeNode>>> = array_to_tree(&input_vec0);
	let obj: Codec = Codec::new();
	let data: String = obj.serialize(root);
	let ans: Option<Rc<RefCell<TreeNode>>> = obj.deserialize(data);
	json!(tree_to_array(&ans))
}
