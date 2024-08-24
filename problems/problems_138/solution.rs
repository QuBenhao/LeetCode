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
		let mut current = head.clone();

        // Step 1: Interleave copied nodes with original nodes
        while let Some(node) = current {
            let copied = Rc::new(RefCell::new(Node::new(node.borrow().val)));
            copied.borrow_mut().next = node.borrow().next.clone();
            node.borrow_mut().next = Some(copied.clone());
            current = copied.borrow().next.clone();
        }

        // Step 2: Assign random pointers for the copied nodes
        current = head.clone();
        while let Some(node) = current {
            if let Some(random) = node.borrow().random.clone() {
                node.borrow().next.clone()?.borrow_mut().random = random.borrow().next.clone();
            }
            let next = node.borrow().next.clone();
            current = next?.borrow().next.clone();
        }

        // Step 3: Separate the copied list from the original list
        current = head.clone();
        let new_head = head.clone()?.borrow().next.clone();

        while let Some(node) = current {
            let next = node.borrow().next.clone();
            node.borrow_mut().next = next.clone()?.borrow().next.clone();
            if let Some(node_next) = node.borrow().next.clone() {
                next?.borrow_mut().next = node_next.borrow().next.clone();
            }
            current = node.borrow().next.clone();
        }

        new_head
    }
}

#[cfg(feature = "solution_138")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let input_vec0: Vec<Vec<Option<i32>>> = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	let head: Option<Rc<RefCell<Node>>> = array_to_node_random(&input_vec0);
	json!(node_random_to_array(&Solution::copy_random_list(head)))
}
