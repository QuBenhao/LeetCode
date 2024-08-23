use serde_json::{json, Value};

use std::{cmp::Reverse, collections::BinaryHeap};

struct MedianFinder {
	left: BinaryHeap<i32>,
	right: BinaryHeap<Reverse<i32>>,
}


/**
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl MedianFinder {

    fn new() -> Self {
		let left = BinaryHeap::new();
		let right = BinaryHeap::new();
		MedianFinder {
			left,
			right
		}
    }
    
    fn add_num(&mut self, num: i32) {
		let left = &mut self.left;
		let right = &mut self.right;
		if left.len() == right.len() {
			if right.is_empty() || num <= right.peek().unwrap().0 {
				left.push(num);
			} else {
				if let Some(v) = right.pop() {
					left.push(v.0);
				}
				right.push(Reverse(num));
			}
		} else {
			if let Some(v) = left.peek() {
				if num >= *v {
					right.push(Reverse(num));
				} else {
					right.push(Reverse(*v));
					left.pop();
					left.push(num);
				}
			}
		}
    }
    
    fn find_median(&self) -> f64 {
		let left = &self.left;
		let right = &self.right;
		if left.len() == right.len() {
			(*left.peek().unwrap() + right.peek().unwrap().0) as f64 / 2.0
		} else {
			*left.peek().unwrap() as f64
		}
    }
}

/**
 * Your MedianFinder object will be instantiated and called as such:
 * let obj = MedianFinder::new();
 * obj.add_num(num);
 * let ret_2: f64 = obj.find_median();
 */

#[cfg(feature = "solution_295")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let operators: Vec<String> = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	let op_values: Vec<Vec<Value>> = serde_json::from_str(&input_values[1]).expect("Failed to parse input");
	let mut obj = MedianFinder::new();
	let mut ans = vec![None];
	for i in 1..operators.len() {
		match operators[i].as_str() {
			"addNum" => {
				let num: i32 = serde_json::from_value(op_values[i][0].clone()).expect("Failed to parse input");
				obj.add_num(num);
				ans.push(None);
			},
			"findMedian" => {
				ans.push(Some(obj.find_median()));
			},
			_ => ans.push(None),
		}
	}
	json!(ans)
}
