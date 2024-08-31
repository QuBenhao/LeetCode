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
use std::collections::HashMap;
impl Solution {
    pub fn path_sum(root: Option<Rc<RefCell<TreeNode>>>, target_sum: i32) -> i32 {
		fn dfs(node: &Option<Rc<RefCell<TreeNode>>>, counter: &mut HashMap<i64, i32>, target_sum: i32, current_sum: i64) -> i32 {
			if node.is_none() {
				return 0;
			}
			let node = node.as_ref().unwrap().borrow();
			let mut res = 0;
			let current_sum = current_sum + node.val as i64;
			res += counter.get(&(current_sum - target_sum as i64)).unwrap_or(&0);
			*counter.entry(current_sum).or_insert(0) += 1;
			res += dfs(&node.left, counter, target_sum, current_sum);
			res += dfs(&node.right, counter, target_sum, current_sum);
			*counter.get_mut(&current_sum).unwrap() -= 1;
			res
		}
		let mut counter = HashMap::new();
		counter.insert(0, 1);
		dfs(&root, &mut counter, target_sum, 0)
    }
}

#[cfg(feature = "solution_437")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let input_vec0: Vec<Option<i32>> = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	let root: Option<Rc<RefCell<TreeNode>>> = array_to_tree(&input_vec0);
	let target_sum: i32 = serde_json::from_str(&input_values[1]).expect("Failed to parse input");
	json!(Solution::path_sum(root, target_sum))
}
