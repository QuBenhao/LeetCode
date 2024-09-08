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
    pub fn max_path_sum(root: Option<Rc<RefCell<TreeNode>>>) -> i32 {
		let mut ans: i32 = i32::MIN;
		fn dfs(node: &Option<Rc<RefCell<TreeNode>>>, ans: &mut i32) -> i32 {
			if let Some(node) = node {
				let left = dfs(&node.borrow().left, ans);
				let right = dfs(&node.borrow().right, ans);
				*ans = (*ans).max(node.borrow().val + left + right);
				0.max(node.borrow().val + left.max(right))
			} else {
				0
			}
		}
		dfs(&root, &mut ans);
		ans
    }
}

#[cfg(feature = "solution_124")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let input_vec0: Vec<Option<i32>> = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	let root: Option<Rc<RefCell<TreeNode>>> = array_to_tree(&input_vec0);
	json!(Solution::max_path_sum(root))
}
