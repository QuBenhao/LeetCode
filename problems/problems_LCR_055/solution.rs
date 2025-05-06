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
struct BSTIterator {

}


/**
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl BSTIterator {

    fn new(root: Option<Rc<RefCell<TreeNode>>>) -> Self {

    }
    
    fn next(&self) -> i32 {

    }
    
    fn has_next(&self) -> bool {

    }
}

/**
 * Your BSTIterator object will be instantiated and called as such:
 * let obj = BSTIterator::new(root);
 * let ret_1: i32 = obj.next();
 * let ret_2: bool = obj.has_next();
 */

#[cfg(feature = "solution_LCR_055")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let operators: Vec<String> = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	let op_values: Vec<Vec<Value>> = serde_json::from_str(&input_values[1]).expect("Failed to parse input");
	let val_obj: i32 = serde_json::from_value(op_values[0][0].clone()).expect("Failed to parse input");
	let mut obj = TreeNode::new(val_obj);
	let root_obj: Option<Rc<RefCell<TreeNode>>> = serde_json::from_value(op_values[0][0].clone()).expect("Failed to parse input");
	let mut obj = TreeNode::new(root_obj);
	let mut ans = vec![None];
	for i in 1..operators.len() {
		match operators[i].as_str() {
			"next" => {
				ans.push(Some(obj.next()));
			},
			"hasNext" => {
				ans.push(Some(obj.has_next()));
			},
			_ => ans.push(None),
		}
	}
	json!(ans)
	let val_obj: i32 = serde_json::from_value(op_values[0][0].clone()).expect("Failed to parse input");
	let mut obj = BSTIterator::new(val_obj);
	let root_obj: Option<Rc<RefCell<TreeNode>>> = serde_json::from_value(op_values[0][0].clone()).expect("Failed to parse input");
	let mut obj = BSTIterator::new(root_obj);
	let mut ans = vec![None];
	for i in 1..operators.len() {
		match operators[i].as_str() {
			"next" => {
				ans.push(Some(obj.next()));
			},
			"hasNext" => {
				ans.push(Some(obj.has_next()));
			},
			_ => ans.push(None),
		}
	}
	json!(ans)
}
