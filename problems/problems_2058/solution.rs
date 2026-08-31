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
    pub fn nodes_between_critical_points(head: Option<Box<ListNode>>) -> Vec<i32> {
        // 最小距离来自相邻临界点，最大距离来自首尾临界点
        let (mut first, mut prev, mut mn) = (0, 0, i32::MAX);
        let mut a = head.as_ref().unwrap();
        let mut b = a.next.as_ref().unwrap();
        let mut c = b.next.as_ref();
        let mut i = 2;
        while let Some(cv) = c {
            if b.val > a.val && b.val > cv.val || b.val < a.val && b.val < cv.val {
                if prev > 0 {
                    mn = mn.min(i - prev);
                } else {
                    first = i;
                }
                prev = i;
            }
            a = b;
            b = cv;
            c = cv.next.as_ref();
            i += 1;
        }
        if mn == i32::MAX {
            vec![-1, -1]
        } else {
            vec![mn, prev - first]
        }
    }
}

#[cfg(feature = "solution_2058")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let input_nums0: Vec<i32> = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	let head: Option<Box<ListNode>> = int_array_to_list_node(&input_nums0);
	json!(Solution::nodes_between_critical_points(head))
}
