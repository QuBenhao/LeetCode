use serde_json::{json, Value};
use library::lib::node_random::{Node, array_to_node_random, node_random_to_array};
pub struct Solution;

// Definition for a Node.
// #[derive(Debug, Clone, PartialEq, Eq)]
// pub struct Node {
//   pub val: i32,
//   pub next: Option<Rc<RefCell<Node>>>,
//   pub random: Option<Rc<RefCell<Node>>>,
// }
//
// impl Node {
//   #[inline]
//   pub fn new(val: i32) -> Self {
//     Node {
//       val,
//       next: None,
//       random: None,
//     }
//   }
// }
use std::rc::Rc;
use std::cell::RefCell;
impl Solution {
    pub fn copy_random_list(head: Option<Rc<RefCell<Node>>>) -> Option<Rc<RefCell<Node>>> {
		return head;
    }
}

#[cfg(feature = "solution_138")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let input_vec0: Vec<Vec<Option<i32>>> = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	let head: Option<Rc<RefCell<Node>>> = array_to_node_random(&input_vec0);
	json!(node_random_to_array(&Solution::copy_random_list(head)))
}
