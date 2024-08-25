use serde_json::{json, Value};
use library::lib::tree_node::{TreeNode, tree_to_array};
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
    pub fn build_tree(preorder: Vec<i32>, inorder: Vec<i32>) -> Option<Rc<RefCell<TreeNode>>> {
		if preorder.is_empty() {
			return None;
		}
		let root_val = preorder[0];
		let root = Some(Rc::new(RefCell::new(TreeNode::new(root_val))));
		let mut root_index = 0;
		for i in 0..inorder.len() {
			if inorder[i] == root_val {
				root_index = i;
				break;
			}
		}
		root.clone()?.borrow_mut().left = Self::build_tree(preorder[1..=root_index].to_vec(), inorder[..root_index].to_vec());
		root.clone()?.borrow_mut().right = Self::build_tree(preorder[root_index + 1..].to_vec(), inorder[root_index + 1..].to_vec());
		root
    }
}

#[cfg(feature = "solution_105")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let preorder: Vec<i32> = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	let inorder: Vec<i32> = serde_json::from_str(&input_values[1]).expect("Failed to parse input");
	json!(tree_to_array(&Solution::build_tree(preorder, inorder)))
}
