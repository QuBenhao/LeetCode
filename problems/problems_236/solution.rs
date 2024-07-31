use serde_json::{json, Value};
use library::lib::tree_node::{TreeNode, tree_to_array, array_to_tree_with_targets};
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
    pub fn lowest_common_ancestor(root: Option<Rc<RefCell<TreeNode>>>, p: Option<Rc<RefCell<TreeNode>>>, q: Option<Rc<RefCell<TreeNode>>>) -> Option<Rc<RefCell<TreeNode>>> {
        if root.is_none() || root == p || root == q {
            return root;
        }
        let left = Solution::lowest_common_ancestor(root.as_ref().unwrap().borrow().left.clone(), p.clone(), q.clone());
        let right = Solution::lowest_common_ancestor(root.as_ref().unwrap().borrow().right.clone(), p.clone(), q.clone());
        if left.is_some() && right.is_some() {
            return root;
        }
        if left.is_some() {
            return left;
        }
        right
    }
}

#[cfg(feature = "solution_236")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let input_vec0: Vec<Option<i32>> = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	let p_val: i32 = serde_json::from_str(&input_values[1]).expect("Failed to parse input");
	let q_val: i32 = serde_json::from_str(&input_values[2]).expect("Failed to parse input");
	let nodes = array_to_tree_with_targets(&input_vec0, vec![p_val, q_val]);
	let root = nodes[0].clone();
	let p = nodes[1].clone();
	let q = nodes[2].clone();
	json!(tree_to_array(&Solution::lowest_common_ancestor(root, p, q)))
}
