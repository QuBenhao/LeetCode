#![allow(non_snake_case)]
use serde_json::{json, Value};


struct RecentCounter {

}


/**
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl RecentCounter {

    fn new() -> Self {

    }
    
    fn ping(&self, t: i32) -> i32 {

    }
}

/**
 * Your RecentCounter object will be instantiated and called as such:
 * let obj = RecentCounter::new();
 * let ret_1: i32 = obj.ping(t);
 */

#[cfg(feature = "solution_LCR_042")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let operators: Vec<String> = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	let op_values: Vec<Vec<Value>> = serde_json::from_str(&input_values[1]).expect("Failed to parse input");
	let mut obj = RecentCounter::new();
	let mut ans = vec![None];
	for i in 1..operators.len() {
		match operators[i].as_str() {
			"ping" => {
				let t: i32 = serde_json::from_value(op_values[i][0].clone()).expect("Failed to parse input");
				ans.push(Some(obj.ping(t)));
			},
			_ => ans.push(None),
		}
	}
	json!(ans)
}
