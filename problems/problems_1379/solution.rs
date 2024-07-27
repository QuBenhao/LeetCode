use serde_json::{json, Value};
use library::lib::tree_node::{TreeNode, array_to_tree, tree_to_array, array_to_tree_with_targets};
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
    pub fn get_target_copy(original: Option<Rc<RefCell<TreeNode>>>, cloned: Option<Rc<RefCell<TreeNode>>>, target: Option<Rc<RefCell<TreeNode>>>) -> Option<Rc<RefCell<TreeNode>>> {
		if original.is_none() || original == target {
			return cloned;
		}
		let left = Solution::get_target_copy(original.as_ref().unwrap().borrow().left.clone(), cloned.as_ref().unwrap().borrow().left.clone(), target.clone());
		if left.is_some() {
			return left;
		}
		Solution::get_target_copy(original.as_ref().unwrap().borrow().right.clone(), cloned.as_ref().unwrap().borrow().right.clone(), target.clone())
    }
}

#[cfg(feature = "solution_1379")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let input_vec0: Vec<Option<i32>> = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	let target_val: i32 = serde_json::from_str(&input_values[1]).expect("Failed to parse input");
	let nodes = array_to_tree_with_targets(&input_vec0, vec![target_val]);
	let original = nodes[0].clone();
	let cloned = array_to_tree(&input_vec0);
	let target = nodes[1].clone();
	json!(tree_to_array(&Solution::get_target_copy(original, cloned, target)))
}
