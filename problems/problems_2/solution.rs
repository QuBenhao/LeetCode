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
    pub fn add_two_numbers(l1: Option<Box<ListNode>>, l2: Option<Box<ListNode>>) -> Option<Box<ListNode>> {
        let mut l1 = l1;
        let mut l2 = l2;
        let mut dummy = Some(Box::new(ListNode::new(0)));
        let mut p = dummy.as_mut().unwrap();
        let mut carry = 0;
        while carry > 0 || l1.is_some() || l2.is_some() {
            if let Some(node) = l1 {
                carry += node.val;
                l1 = node.next;
            }
            if let Some(node) = l2 {
                carry += node.val;
                l2 = node.next;
            }
            p.next = Some(Box::new(ListNode::new(carry % 10)));
            p = p.next.as_mut().unwrap();
            carry = carry / 10;
        }
        dummy.unwrap().next
    }
}

#[cfg(feature = "solution_2")]
pub fn solve(input_string: String) -> Value {
    let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
    let nums0: Vec<i32> = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
    let nums1: Vec<i32> = serde_json::from_str(&input_values[1]).expect("Failed to parse input");
    let l1: Option<Box<ListNode>> = int_array_to_list_node(&nums0);
    let l2: Option<Box<ListNode>> = int_array_to_list_node(&nums1);
    json!(list_node_to_int_array(&Solution::add_two_numbers(l1, l2)))
}