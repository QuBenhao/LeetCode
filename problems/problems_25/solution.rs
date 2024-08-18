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
    pub fn reverse_k_group(mut head: Option<Box<ListNode>>, k: i32) -> Option<Box<ListNode>> {
        let mut next_head = &mut head;
        // 获取下一轮头结点
        for _ in 0..k {
            if let Some(node) = next_head.as_mut() {
                next_head = &mut node.next;
            } else {
                return head;
            }
        }
        // 获取除本轮结果
        let mut new_head = Self::reverse_k_group(next_head.take(), k);
        // 翻转本轮k个节点
        for _ in 0..k {
            if let Some(mut node) = head {
                head = node.next.take();
                node.next = new_head.take();
                new_head = Some(node);
            }
        }
        new_head
    }
}

#[cfg(feature = "solution_25")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let input_nums0: Vec<i32> = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	let head: Option<Box<ListNode>> = int_array_to_list_node(&input_nums0);
	let k: i32 = serde_json::from_str(&input_values[1]).expect("Failed to parse input");
	json!(list_node_to_int_array(&Solution::reverse_k_group(head, k)))
}
