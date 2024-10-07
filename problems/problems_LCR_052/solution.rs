#![allow(non_snake_case)]
use serde_json::{json, Value};
use library::lib::tree_node::{TreeNode, array_to_tree, tree_to_array};
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
use std::collections::VecDeque;
use std::rc::Rc;
use std::cell::RefCell;
impl Solution {
    pub fn increasing_bst(root: Option<Rc<RefCell<TreeNode>>>) -> Option<Rc<RefCell<TreeNode>>> {
        let mut stk = VecDeque::new();
        
        fn dfs(root: Option<Rc<RefCell<TreeNode>>>, stk: &mut VecDeque<Rc<RefCell<TreeNode>>>) {
            if let Some(root) = root {
                let tr = Rc::clone(&root);
                dfs(tr.borrow_mut().left.take(), stk);
                stk.push_back(root);
                dfs(tr.borrow_mut().right.take(), stk);
            }        
        }
        
        dfs(root, &mut stk);
        
        let mut head = None;
        while let Some(last) = stk.pop_back() {
            last.borrow_mut().right = head;
            head = Some(last);
        }
        head
    }
}

#[cfg(feature = "solution_LCR_052")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let input_vec0: Vec<Option<i32>> = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	let root: Option<Rc<RefCell<TreeNode>>> = array_to_tree(&input_vec0);
	json!(tree_to_array(&Solution::increasing_bst(root)))
}
