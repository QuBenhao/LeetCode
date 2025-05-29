#![allow(non_snake_case)]
use serde_json::{json, Value};


struct Solution {

}


/**
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl Solution {

    fn new(w: Vec<i32>) -> Self {

    }
    
    fn pick_index(&self) -> i32 {

    }
}

/**
 * Your Solution object will be instantiated and called as such:
 * let obj = Solution::new(w);
 * let ret_1: i32 = obj.pick_index();
 */

#[cfg(feature = "solution_LCR_071")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let operators: Vec<String> = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	let op_values: Vec<Vec<Value>> = serde_json::from_str(&input_values[1]).expect("Failed to parse input");
	let w_obj: Vec<i32> = serde_json::from_value(op_values[0][0].clone()).expect("Failed to parse input");
	let mut obj = Solution::new(w_obj);
	let mut ans = vec![None];
	for i in 1..operators.len() {
		match operators[i].as_str() {
			"pickIndex" => {
				ans.push(Some(obj.pick_index()));
			},
			_ => ans.push(None),
		}
	}
	json!(ans)
}
