#![allow(non_snake_case)]
use serde_json::{json, Value};
use library::lib::tree_node::{TreeNode, array_to_tree, tree_to_array};
pub struct Solution;

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
impl Solution {
    pub fn prune_tree(root: Option<Rc<RefCell<TreeNode>>>) -> Option<Rc<RefCell<TreeNode>>> {
		if let Some(node) = root.clone() {
			let left = node.borrow_mut().left.take();
			let right = node.borrow_mut().right.take();
			node.borrow_mut().left = Self::prune_tree(left);
			node.borrow_mut().right = Self::prune_tree(right);
			if node.borrow().val == 0 && node.borrow().left.is_none() && node.borrow().right.is_none() {
				return None;
			}
		}
		root
    }
}

#[cfg(feature = "solution_LCR_047")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let input_vec0: Vec<Option<i32>> = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	let root: Option<Rc<RefCell<TreeNode>>> = array_to_tree(&input_vec0);
	json!(tree_to_array(&Solution::prune_tree(root)))
}
