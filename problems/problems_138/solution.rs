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
            let new_node = Rc::new(RefCell::new(Node::new(node.borrow().val)));
            new_node.borrow_mut().next = node.borrow().next.clone();
            node.borrow_mut().next = Some(new_node.clone());
            current = new_node.borrow().next.clone();
        }

        // Step 2: Assign random pointers for the copied nodes
        current = head.clone();
        while let Some(node) = current {
            if let Some(random) = &node.borrow().random {
                node.borrow().next.as_ref()?.borrow_mut().random = random.borrow().next.clone();
            }
            current = node.borrow().next.as_ref()?.borrow().next.clone();
        }

        // Step 3: Separate the copied list from the original list
        current = head.clone();
        let mut new_head = None;
        let mut new_current = None;

        while let Some(node) = current {
            let copied_node = node.borrow().next.clone()?;
            node.borrow_mut().next = copied_node.borrow().next.clone();

            if new_head.is_none() {
                new_head = Some(copied_node.clone());
                new_current = Some(copied_node);
            } else {
                new_current.as_ref()?.borrow_mut().next = Some(copied_node.clone());
                new_current = Some(copied_node);
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
