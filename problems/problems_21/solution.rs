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
    pub fn merge_two_lists(list1: Option<Box<ListNode>>, list2: Option<Box<ListNode>>) -> Option<Box<ListNode>> {
		let mut dummy = ListNode::new(0);
		let mut node = &mut dummy;
		let mut list1 = list1;
		let mut list2 = list2;
		while list1.is_some() && list2.is_some() {
			if list1.as_ref().unwrap().val < list2.as_ref().unwrap().val {
				let next = list1.as_mut().unwrap().next.take();
				node.next = list1;
				list1 = next;
			} else {
				let next = list2.as_mut().unwrap().next.take();
				node.next = list2;
				list2 = next;
			}
			node = node.next.as_mut().unwrap();
		}
		node.next = list1.or(list2);
		dummy.next
    }
}

#[cfg(feature = "solution_21")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let input_nums0: Vec<i32> = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	let list1: Option<Box<ListNode>> = int_array_to_list_node(&input_nums0);
	let input_nums1: Vec<i32> = serde_json::from_str(&input_values[1]).expect("Failed to parse input");
	let list2: Option<Box<ListNode>> = int_array_to_list_node(&input_nums1);
	json!(list_node_to_int_array(&Solution::merge_two_lists(list1, list2)))
}
