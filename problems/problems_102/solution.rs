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
		let mut ans = vec![];
		if root.is_none() {
			return ans
		}
		let mut queue = VecDeque::new();
		queue.push_back(root.clone().unwrap());
		while !queue.is_empty() {
			let mut cur = vec![];
			for _ in 0..queue.len() {
				let node = queue.pop_front().unwrap();
				cur.push(node.borrow().val);
				if node.borrow().left.is_some() {
					queue.push_back(node.borrow().left.clone().unwrap());
				}
				if node.borrow().right.is_some() {
					queue.push_back(node.borrow().right.clone().unwrap());
				}
			}
			ans.push(cur);
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
