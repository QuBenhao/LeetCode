#![allow(non_snake_case)]
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
struct Codec {
	
}

/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl Codec {
    fn new() -> Self {
        
    }

    fn serialize(&self, root: Option<Rc<RefCell<TreeNode>>>) -> String {
        
    }
	
    fn deserialize(&self, data: String) -> Option<Rc<RefCell<TreeNode>>> {
        
    }
}

/**
 * Your Codec object will be instantiated and called as such:
 * let obj = Codec::new();
 * let data: String = obj.serialize(strs);
 * let ans: Option<Rc<RefCell<TreeNode>>> = obj.deserialize(data);
 */

#[cfg(feature = "solution_LCR_048")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let operators: Vec<String> = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	let op_values: Vec<Vec<Value>> = serde_json::from_str(&input_values[1]).expect("Failed to parse input");
	let val_obj: i32 = serde_json::from_value(op_values[0][0].clone()).expect("Failed to parse input");
	let mut obj = TreeNode::new(val_obj);
	let mut obj = TreeNode::new();
	let mut ans = vec![None];
	for i in 1..operators.len() {
		match operators[i].as_str() {
			"serialize" => {
				let root: Option<Rc<RefCell<TreeNode>>> = serde_json::from_value(op_values[i][0].clone()).expect("Failed to parse input");
				ans.push(Some(obj.serialize(root)));
			},
			"deserialize" => {
				let data: String = serde_json::from_value(op_values[i][0].clone()).expect("Failed to parse input");
				ans.push(Some(obj.deserialize(data)));
			},
			_ => ans.push(None),
		}
	}
	json!(ans)
	let val_obj: i32 = serde_json::from_value(op_values[0][0].clone()).expect("Failed to parse input");
	let mut obj = Codec::new(val_obj);
	let mut obj = Codec::new();
	let mut ans = vec![None];
	for i in 1..operators.len() {
		match operators[i].as_str() {
			"serialize" => {
				let root: Option<Rc<RefCell<TreeNode>>> = serde_json::from_value(op_values[i][0].clone()).expect("Failed to parse input");
				ans.push(Some(obj.serialize(root)));
			},
			"deserialize" => {
				let data: String = serde_json::from_value(op_values[i][0].clone()).expect("Failed to parse input");
				ans.push(Some(obj.deserialize(data)));
			},
			_ => ans.push(None),
		}
	}
	json!(ans)
}
