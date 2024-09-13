#![allow(non_snake_case)]
use library::lib::tree_node::{TreeNode, array_to_tree,  tree_to_array};
use serde_json::{json, Value};


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
struct CBTInserter {
    root: Rc<RefCell<TreeNode>>,
    fifo: VecDeque<Rc<RefCell<TreeNode>>>,
}

impl CBTInserter {

    fn new(root: Option<Rc<RefCell<TreeNode>>>) -> Self {
        let root = root.unwrap();
        let mut fifo = VecDeque::new();
        fifo.push_back(root.clone());
        loop {
            let t = fifo.pop_front().unwrap();
            if t.borrow().right.is_none() {fifo.push_front(t); break}
            fifo.push_back(t.borrow().left.as_ref().unwrap().clone());
            fifo.push_back(t.borrow().right.as_ref().unwrap().clone());
        }
        Self {root, fifo}
    }

    fn insert(&mut self, v: i32) -> i32 {
        let t = self.fifo.pop_front().unwrap();
        let ans = t.borrow().val;
        if t.borrow().left.is_none() {
            t.borrow_mut().left = Some(Rc::new(RefCell::new(TreeNode::new(v))));
            self.fifo.push_front(t);
        } else {
            t.borrow_mut().right = Some(Rc::new(RefCell::new(TreeNode::new(v))));
            self.fifo.push_back(t.borrow().left.as_ref().unwrap().clone());
            self.fifo.push_back(t.borrow().right.as_ref().unwrap().clone());
        }
        ans
    }

    fn get_root(&self) -> Option<Rc<RefCell<TreeNode>>> {
        Some(self.root.clone())
    }
}

/**
 * Your CBTInserter object will be instantiated and called as such:
 * let obj = CBTInserter::new(root);
 * let ret_1: i32 = obj.insert(v);
 * let ret_2: Option<Rc<RefCell<TreeNode>>> = obj.get_root();
 */

#[cfg(feature = "solution_LCR_043")]
pub fn solve(input_string: String) -> Value {
    let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
    let operators: Vec<String> = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
    let op_values: Vec<Vec<Value>> = serde_json::from_str(&input_values[1]).expect("Failed to parse input");
	let root_vec: Vec<Option<i32>> = serde_json::from_value(op_values[0][0].clone()).expect("Failed to parse input");
    let root_obj: Option<Rc<RefCell<TreeNode>>> = array_to_tree(&root_vec);
    let mut obj = CBTInserter::new(root_obj);
    let mut ans: Vec<Option<Value>> = vec![None];
    for i in 1..operators.len() {
        match operators[i].as_str() {
            "insert" => {
                let v: i32 = serde_json::from_value(op_values[i][0].clone()).expect("Failed to parse input");
                ans.push(Some(Value::from(obj.insert(v))));
            },
            "get_root" => {
                ans.push(Some(Value::from(tree_to_array(&obj.get_root()))));
            },
            _ => ans.push(None),
        }
    }
    json!(ans)
}