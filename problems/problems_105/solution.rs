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

    }
}

#[cfg(feature = "solution_105")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let preorder: Vec<i32> = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	let inorder: Vec<i32> = serde_json::from_str(&input_values[1]).expect("Failed to parse input");
	json!(tree_to_array(&Solution::build_tree(preorder, inorder)))
}
