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
use std::collections::BinaryHeap;
use std::cmp::Reverse;

impl Solution {
    pub fn merge_k_lists(lists: Vec<Option<Box<ListNode>>>) -> Option<Box<ListNode>> {
        let mut ans=Box::new(ListNode::new(0));
        let mut pans=&mut ans;
        let mut heap = BinaryHeap::new();
        for list in lists{
            let mut plist = &list;
            while let Some(node) = plist{
                heap.push(Reverse(node.val));
                plist=&node.next;
            }
        }
        while let Some(Reverse(n)) = heap.pop(){
            pans.next=Some(Box::new(ListNode::new(n)));
            pans=pans.next.as_mut().unwrap();
        }
        ans.next
    }
}

#[cfg(feature = "solution_23")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let input_nums0: Vec<Vec<i32>> = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	let lists: Vec<Option<Box<ListNode>>> = input_nums0.into_iter().map(|nums| int_array_to_list_node(&nums)).collect();
	json!(list_node_to_int_array(&Solution::merge_k_lists(lists)))
}
