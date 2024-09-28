#![allow(non_snake_case)]
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
    pub fn largest_values(root: Option<Rc<RefCell<TreeNode>>>) -> Vec<i32> {
		let mut res = vec![];
		if root.is_none() {
			return res;
		}
		let mut queue = VecDeque::new();
		queue.push_back(root);
		while !queue.is_empty() {
			let mut max = i32::MIN;
			let len = queue.len();
			for _ in 0..len {
				let node = queue.pop_front().unwrap();
				let node = node.unwrap();
				let node = node.borrow();
				max = max.max(node.val);
				if node.left.is_some() {
					queue.push_back(node.left.clone());
				}
				if node.right.is_some() {
					queue.push_back(node.right.clone());
				}
			}
			res.push(max);
		}
		res
    }
}

#[cfg(feature = "solution_LCR_044")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let input_vec0: Vec<Option<i32>> = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	let root: Option<Rc<RefCell<TreeNode>>> = array_to_tree(&input_vec0);
	json!(Solution::largest_values(root))
}
