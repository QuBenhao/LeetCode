#![allow(non_snake_case)]
use library::lib::tree_node::{array_to_tree, TreeNode};
use serde_json::{json, Value};
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
use std::cell::RefCell;
use std::collections::HashMap;
use std::rc::Rc;
impl Solution {
    pub fn path_sum(root: Option<Rc<RefCell<TreeNode>>>, target_sum: i32) -> i32 {
        let mut counter: HashMap<i64, i32> = HashMap::new();
        counter.insert(0, 1);
        fn dfs(
            node: &Option<Rc<RefCell<TreeNode>>>,
            mut cur: i64,
            map: &mut HashMap<i64, i32>,
            target_sum: i64,
        ) -> i32 {
            if let Some(nd) = node {
                cur += nd.borrow().val as i64;
                let mut ans: i32 = 0;
                ans += map.get(&(cur - target_sum)).unwrap_or(&0);
                map.insert(cur, map.get(&cur).unwrap_or(&0) + 1);
                ans += dfs(&nd.borrow().left, cur, map, target_sum);
                ans += dfs(&nd.borrow().right, cur, map, target_sum);
                map.insert(cur, map.get(&cur).unwrap_or(&0) - 1);
                ans
            } else {
                0
            }
        }
        dfs(&root, 0, &mut counter, target_sum as i64)
    }
}

#[cfg(feature = "solution_LCR_050")]
pub fn solve(input_string: String) -> Value {
    let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
    let input_vec0: Vec<Option<i32>> =
        serde_json::from_str(&input_values[0]).expect("Failed to parse input");
    let root: Option<Rc<RefCell<TreeNode>>> = array_to_tree(&input_vec0);
    let target_sum: i32 = serde_json::from_str(&input_values[1]).expect("Failed to parse input");
    json!(Solution::path_sum(root, target_sum))
}
