use serde_json::{json, Value};
use library::lib::tree_node::{TreeNode, array_to_tree};
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
	fn dfs(node: Option<Rc<RefCell<TreeNode>>>, sub_root: Option<Rc<RefCell<TreeNode>>>, must_match: bool) -> bool {
		if node.is_none() || sub_root.is_none() {
			return node.is_none() && sub_root.is_none();
		}
		let nd = node.as_ref().unwrap().borrow();
		let sd = sub_root.as_ref().unwrap().borrow();
		if nd.val == sd.val && Solution::dfs(nd.left.clone(), sd.left.clone(), true) && Solution::dfs(nd.right.clone(), sd.right.clone(), true) {
			return true;
		}
		if must_match {
			return false
		}
		Solution::dfs(nd.left.clone(), sub_root.clone(), false) || Solution::dfs(nd.right.clone(), sub_root.clone(), false)
	}
    pub fn is_subtree(root: Option<Rc<RefCell<TreeNode>>>, sub_root: Option<Rc<RefCell<TreeNode>>>) -> bool {
		Solution::dfs(root, sub_root, false)
    }
}

#[cfg(feature = "solution_572")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let input_vec0: Vec<Option<i32>> = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	let root: Option<Rc<RefCell<TreeNode>>> = array_to_tree(&input_vec0);
	let input_vec1: Vec<Option<i32>> = serde_json::from_str(&input_values[1]).expect("Failed to parse input");
	let sub_root: Option<Rc<RefCell<TreeNode>>> = array_to_tree(&input_vec1);
	json!(Solution::is_subtree(root, sub_root))
}
