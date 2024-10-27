#![allow(non_snake_case)]
use serde_json::{json, Value};
use library::lib::tree_node::{TreeNode, tree_to_array, array_to_tree_with_targets};
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
    pub fn inorder_successor(root: Option<Rc<RefCell<TreeNode>>>, p: Option<Rc<RefCell<TreeNode>>>) -> Option<Rc<RefCell<TreeNode>>> {
		let mut stack = vec![];
		let mut found = false;
		let mut node = root.clone();
		while node.is_some() || !stack.is_empty() {
			while let Some(n) = node {
				stack.push(n.clone());
				node = n.borrow().left.clone();
			}
			node = stack.pop();
			if found {
				return node;
			}
			if node == p {
				found = true;
			}
			node = node.unwrap().borrow().right.clone();
		}
		None
    }
}

#[cfg(feature = "solution_LCR_053")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let input_vec0: Vec<Option<i32>> = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	let p_val: i32 = serde_json::from_str(&input_values[1]).expect("Failed to parse input");
	let nodes = array_to_tree_with_targets(&input_vec0, vec![p_val]);
	let root = nodes[0].clone();
	let p = nodes[1].clone();
	json!(tree_to_array(&Solution::inorder_successor(root, p)))
}
