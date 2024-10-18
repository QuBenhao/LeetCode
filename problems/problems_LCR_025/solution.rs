#![allow(non_snake_case)]
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
        
    }
}

#[cfg(feature = "solution_LCR_025")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let input_nums0: Vec<i32> = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	let l1: Option<Box<ListNode>> = int_array_to_list_node(&input_nums0);
	let input_nums1: Vec<i32> = serde_json::from_str(&input_values[1]).expect("Failed to parse input");
	let l2: Option<Box<ListNode>> = int_array_to_list_node(&input_nums1);
	json!(list_node_to_int_array(&Solution::add_two_numbers(l1, l2)))
}
