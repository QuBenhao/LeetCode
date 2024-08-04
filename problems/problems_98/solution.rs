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
	fn dfs(node: Option<Rc<RefCell<TreeNode>>>, lower: i64, upper: i64) -> bool {
		if node.is_none() {
			return true;
		}
		let nd = node.as_ref().unwrap().borrow();
		if nd.val as i64 <= lower || nd.val as i64 >= upper {
			return false;
		}
		Solution::dfs(nd.left.clone(), lower, nd.val as i64) && Solution::dfs(nd.right.clone(), nd.val as i64, upper)
	}

    pub fn is_valid_bst(root: Option<Rc<RefCell<TreeNode>>>) -> bool {
		Solution::dfs(root, i64::MIN, i64::MAX)
    }
}

#[cfg(feature = "solution_98")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let input_vec0: Vec<Option<i32>> = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	let root: Option<Rc<RefCell<TreeNode>>> = array_to_tree(&input_vec0);
	json!(Solution::is_valid_bst(root))
}
