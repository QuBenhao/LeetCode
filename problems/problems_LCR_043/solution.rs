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
struct CBTInserter {

}


/**
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl CBTInserter {

    fn new(root: Option<Rc<RefCell<TreeNode>>>) -> Self {

    }
    
    fn insert(&self, v: i32) -> i32 {

    }
    
    fn get_root(&self) -> Option<Rc<RefCell<TreeNode>>> {

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
	let val_obj: i32 = serde_json::from_value(op_values[0][0].clone()).expect("Failed to parse input");
	let mut obj = TreeNode::new(val_obj);
	let root_obj: Option<Rc<RefCell<TreeNode>>> = serde_json::from_value(op_values[0][0].clone()).expect("Failed to parse input");
	let mut obj = TreeNode::new(root_obj);
	let mut ans = vec![None];
	for i in 1..operators.len() {
		match operators[i].as_str() {
			"insert" => {
				let v: i32 = serde_json::from_value(op_values[i][0].clone()).expect("Failed to parse input");
				ans.push(Some(obj.insert(v)));
			},
			"getRoot" => {
				ans.push(Some(obj.get_root()));
			},
			_ => ans.push(None),
		}
	}
	json!(ans)
	let val_obj: i32 = serde_json::from_value(op_values[0][0].clone()).expect("Failed to parse input");
	let mut obj = CBTInserter::new(val_obj);
	let root_obj: Option<Rc<RefCell<TreeNode>>> = serde_json::from_value(op_values[0][0].clone()).expect("Failed to parse input");
	let mut obj = CBTInserter::new(root_obj);
	let mut ans = vec![None];
	for i in 1..operators.len() {
		match operators[i].as_str() {
			"insert" => {
				let v: i32 = serde_json::from_value(op_values[i][0].clone()).expect("Failed to parse input");
				ans.push(Some(obj.insert(v)));
			},
			"getRoot" => {
				ans.push(Some(obj.get_root()));
			},
			_ => ans.push(None),
		}
	}
	json!(ans)
}
