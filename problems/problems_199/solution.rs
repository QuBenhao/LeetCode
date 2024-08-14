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
use std::cell::{Ref, RefCell};
use std::collections::VecDeque;

impl Solution {
    pub fn right_side_view(root: Option<Rc<RefCell<TreeNode>>>) -> Vec<i32> {
		let mut res: Vec<i32> = Vec::new();
		if root.is_none() {
			return res;
		}
		let mut queue: VecDeque<Option<Rc<RefCell<TreeNode>>>> = VecDeque::new();
		queue.push_back(root);
		while !queue.is_empty() {
			let n = queue.len();
			for i in 0..n {
				if let Some(node) = queue.pop_front().as_ref().unwrap() {
					let node_ref: Ref<TreeNode> = node.borrow();
					if i == n - 1 {
						res.push(node_ref.val);
					}
					if node_ref.left.is_some() {
						queue.push_back(node_ref.left.clone());
					}
					if node_ref.right.is_some() {
						queue.push_back(node_ref.right.clone());
					}
				}
			}
		}
		res
    }
}

#[cfg(feature = "solution_199")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let input_vec0: Vec<Option<i32>> = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	let root: Option<Rc<RefCell<TreeNode>>> = array_to_tree(&input_vec0);
	json!(Solution::right_side_view(root))
}
