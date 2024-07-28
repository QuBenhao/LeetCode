use serde_json::{json, Value};
use library::lib::node_next::{Node, array_to_tree_next, tree_next_to_array};
pub struct Solution;

/*
// Definition for a Node.
#[derive(Debug, PartialEq, Eq)]
pub struct Node {
    pub val: i32,
    pub left: Option<Rc<RefCell<Node>>>, // left child
    pub right: Option<Rc<RefCell<Node>>>, // right child
    pub next: Option<Rc<RefCell<Node>>>, // next child
}
*/
use std::cell::RefCell;
use std::rc::Rc;
impl Solution {
    pub fn connect(root: Option<Rc<RefCell<Node>>>) -> Option<Rc<RefCell<Node>>> {
		if root.is_none() {
			return None;
		}
		let mut head = root.clone();
		while head.is_some() {
			let mut cur = head.clone();
			head = None;
			let mut pre: Option<Rc<RefCell<Node>>> = None;
			while cur.is_some() {
				let node = cur.as_ref().unwrap().borrow();
				if node.left.is_some() {
					if pre.is_some() {
						pre.as_ref().unwrap().borrow_mut().next = node.left.clone();
					} else {
						head = node.left.clone();
					}
					pre = node.left.clone();
				}
				if node.right.is_some() {
					if pre.is_some() {
						pre.as_ref().unwrap().borrow_mut().next = node.right.clone();
					} else {
						head = node.right.clone();
					}
					pre = node.right.clone();
				}
				let next = cur.as_ref().unwrap().borrow().next.clone();
				drop(node);
				cur = next;
			}
		}
		root
    }
}

#[cfg(feature = "solution_117")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let input_vec0: Vec<Option<i32>> = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	let root: Option<Rc<RefCell<Node>>> = array_to_tree_next(&input_vec0);
	json!(tree_next_to_array(&Solution::connect(root)))
}
