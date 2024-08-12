use serde_json::{json, Value};
use library::lib::list_node::{ListNode, int_array_to_list_node, list_node_to_int_array};
pub struct Solution;

// Definition for singly-linked list.
// #[derive(PartialEq, Eq, Clone, Debug)]
// pub struct ListNode {
//   pub val: i32,
//   pub next: Option<Box<ListNode>>
// }
//
// impl ListNode {
//   #[inline]
//   fn new(val: i32) -> Self {
//     ListNode {
//       next: None,
//       val
//     }
//   }
// }
impl Solution {
    pub fn swap_pairs(head: Option<Box<ListNode>>) -> Option<Box<ListNode>> {
		let mut dummy: ListNode = ListNode::new(0);
		dummy.next = head;
		let mut prev: &mut ListNode = &mut dummy;
		while prev.next.is_some() && prev.next.as_ref()?.next.is_some() {
			let mut node1: Box<ListNode> = prev.next.take()?;
			let mut node2: Box<ListNode> = node1.next.take()?;
			node1.next = node2.next.take();
			node2.next = Some(node1);
			prev.next = Some(node2);
			prev = prev.next.as_mut()?.next.as_mut()?;
		}
		dummy.next
    }
}

#[cfg(feature = "solution_24")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let input_nums0: Vec<i32> = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	let head: Option<Box<ListNode>> = int_array_to_list_node(&input_nums0);
	json!(list_node_to_int_array(&Solution::swap_pairs(head)))
}
