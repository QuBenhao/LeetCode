use serde_json::{json, Value};
use library::lib::list_node::{ListNode, int_array_to_list_node};
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
    pub fn get_decimal_value(head: Option<Box<ListNode>>) -> i32 {
        
    }
}

#[cfg(feature = "solution_1290")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let input_nums0: Vec<i32> = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	let head: Option<Box<ListNode>> = int_array_to_list_node(&input_nums0);
	json!(Solution::get_decimal_value(head))
}
