#![allow(non_snake_case)]
use serde_json::{json, Value};

use std::cmp::Reverse;
use std::collections::BinaryHeap;
struct KthLargest {
	k: i32,
	heap: BinaryHeap<Reverse<i32>>,
}


/**
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl KthLargest {

    fn new(k: i32, nums: Vec<i32>) -> Self {
		let mut heap = BinaryHeap::new();
		for num in nums {
			heap.push(Reverse(num));
			if heap.len() > k as usize {
				heap.pop();
			}
		}
		KthLargest {
			k,
			heap
		}
    }
    
    fn add(&mut self, val: i32) -> i32 {
		self.heap.push(Reverse(val));
		if self.heap.len() > self.k as usize {
			self.heap.pop();
		}
		self.heap.peek().unwrap().0
    }
}

/**
 * Your KthLargest object will be instantiated and called as such:
 * let obj = KthLargest::new(k, nums);
 * let ret_1: i32 = obj.add(val);
 */

#[cfg(feature = "solution_LCR_059")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let operators: Vec<String> = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	let op_values: Vec<Vec<Value>> = serde_json::from_str(&input_values[1]).expect("Failed to parse input");
	let k_obj: i32 = serde_json::from_value(op_values[0][0].clone()).expect("Failed to parse input");
	let nums_obj: Vec<i32> = serde_json::from_value(op_values[0][1].clone()).expect("Failed to parse input");
	let mut obj = KthLargest::new(k_obj, nums_obj);
	let mut ans = vec![None];
	for i in 1..operators.len() {
		match operators[i].as_str() {
			"add" => {
				let val: i32 = serde_json::from_value(op_values[i][0].clone()).expect("Failed to parse input");
				ans.push(Some(obj.add(val)));
			},
			_ => ans.push(None),
		}
	}
	json!(ans)
}
