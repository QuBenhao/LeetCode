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
    pub fn flatten(root: &mut Option<Rc<RefCell<TreeNode>>>) {
		if let Some(root) = root {
			let root_clone = root.clone();
			let mut mut_root = root_clone.borrow_mut();
			Self::flatten(&mut mut_root.left);
			Self::flatten(&mut mut_root.right);
			let left = mut_root.left.take();
			let right = mut_root.right.take();
			mut_root.right = left;
			drop(mut_root);
			let mut cur = root.clone();
			while cur.borrow().right.is_some() {
				let next = cur.borrow().right.clone().unwrap();
				cur = next;
			}
			cur.borrow_mut().right = right;
		}
    }
}

#[cfg(feature = "solution_114")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let input_vec0: Vec<Option<i32>> = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	let mut root: Option<Rc<RefCell<TreeNode>>> = array_to_tree(&input_vec0);
	Solution::flatten(&mut root);
	json!(tree_to_array(&root))
}
