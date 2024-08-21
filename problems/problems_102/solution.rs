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
use std::collections::VecDeque;
impl Solution {
    pub fn level_order(root: Option<Rc<RefCell<TreeNode>>>) -> Vec<Vec<i32>> {
		let mut ans: Vec<Vec<i32>> = Vec::new();
		if let Some(root) = root {
			let mut queue = VecDeque::new();
			queue.push_back(root);
			while !queue.is_empty() {
				let size = queue.len();
				let mut level = Vec::new();
				for _ in 0..size {
					if let Some(node) = queue.pop_front() {
						level.push(node.borrow().val);
						if let Some(left) = node.borrow().left.clone() {
							queue.push_back(left);
						}
						if let Some(right) = node.borrow().right.clone() {
							queue.push_back(right);
						}
					}
				}
				ans.push(level);
			}
		}
		ans
    }
}

#[cfg(feature = "solution_102")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let input_vec0: Vec<Option<i32>> = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	let root: Option<Rc<RefCell<TreeNode>>> = array_to_tree(&input_vec0);
	json!(Solution::level_order(root))
}
