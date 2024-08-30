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
    pub fn sort_list(mut head: Option<Box<ListNode>>) -> Option<Box<ListNode>> {
		if head.is_none() || head.as_ref()?.next.is_none() {
			return head;
		}
		let mut len = 0;
		let mut ptr = &head;
		while let Some(node) = ptr {
			ptr = &node.next;
			len += 1;
		}
		let mut ptr = &mut head;
		for _ in 0..len/2 {
			if let Some(ref mut node) = ptr {
				ptr = &mut node.next;
			}
		}
		let next = ptr.take();
		let mut left = Self::sort_list(head);
		let mut right = Self::sort_list(next);
		let mut dummy = Some(Box::new(ListNode { val: 0, next: None }));
		let mut curr = dummy.as_mut();
		while left.is_some() && right.is_some() {
			if left.as_ref().unwrap().val < right.as_ref().unwrap().val {
				let temp = left.as_mut().unwrap().next.take();
				curr.as_mut().unwrap().next = left;
				left = temp;
			} else {
				let temp: Option<Box<ListNode>> = right.as_mut().unwrap().next.take();
				curr.as_mut().unwrap().next = right;
				right = temp;
			}
			curr = curr.unwrap().next.as_mut();
		}
		if left.is_some() {
			curr.as_mut().unwrap().next = left;
		} else {
			curr.as_mut().unwrap().next = right;
		}
		dummy?.next
    }
}

#[cfg(feature = "solution_148")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let input_nums0: Vec<i32> = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	let head: Option<Box<ListNode>> = int_array_to_list_node(&input_nums0);
	json!(list_node_to_int_array(&Solution::sort_list(head)))
}
