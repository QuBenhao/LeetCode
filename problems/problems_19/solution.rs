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
    pub fn remove_nth_from_end(head: Option<Box<ListNode>>, n: i32) -> Option<Box<ListNode>> {
		let mut dummy = Some(Box::new(ListNode { val: 0, next: head }));
		let mut slow = &mut dummy;
		let mut fast = &slow.clone();
		for _ in 0..=n {
			if let Some(fast_node) = fast {
				fast = &fast_node.next;
			} else {
				return None;
			}
		}
		while fast.is_some() {
			slow = &mut slow.as_mut()?.next;
			fast = &fast.as_ref()?.next;
		}
		let remove_node = &mut slow.as_mut()?.next;
		slow.as_mut()?.next = remove_node.as_mut()?.next.take();
		dummy?.next
    }
}

#[cfg(feature = "solution_19")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let input_nums0: Vec<i32> = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	let head: Option<Box<ListNode>> = int_array_to_list_node(&input_nums0);
	let n: i32 = serde_json::from_str(&input_values[1]).expect("Failed to parse input");
	json!(list_node_to_int_array(&Solution::remove_nth_from_end(head, n)))
}
