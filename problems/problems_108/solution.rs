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
    pub fn sorted_array_to_bst(nums: Vec<i32>) -> Option<Rc<RefCell<TreeNode>>> {
		if nums.is_empty() {
			return None;
		}
		let mid = nums.len() / 2;
		let mut root = TreeNode::new(nums[mid]);
		root.left = Solution::sorted_array_to_bst(nums[..mid].to_vec());
		root.right = Solution::sorted_array_to_bst(nums[mid + 1..].to_vec());
		Some(Rc::new(RefCell::new(root)))
    }
}

#[cfg(feature = "solution_108")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let nums: Vec<i32> = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	json!(tree_to_array(&Solution::sorted_array_to_bst(nums)))
}
