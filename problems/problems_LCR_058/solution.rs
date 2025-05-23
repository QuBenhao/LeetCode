#![allow(non_snake_case)]
use serde_json::{json, Value};


struct MyCalendar {

}


/**
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl MyCalendar {

    fn new() -> Self {

    }
    
    fn book(&self, start: i32, end: i32) -> bool {

    }
}

/**
 * Your MyCalendar object will be instantiated and called as such:
 * let obj = MyCalendar::new();
 * let ret_1: bool = obj.book(start, end);
 */

#[cfg(feature = "solution_LCR_058")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let operators: Vec<String> = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	let op_values: Vec<Vec<Value>> = serde_json::from_str(&input_values[1]).expect("Failed to parse input");
	let mut obj = MyCalendar::new();
	let mut ans = vec![None];
	for i in 1..operators.len() {
		match operators[i].as_str() {
			"book" => {
				let start: i32 = serde_json::from_value(op_values[i][0].clone()).expect("Failed to parse input");
				let end: i32 = serde_json::from_value(op_values[i][1].clone()).expect("Failed to parse input");
				ans.push(Some(obj.book(start, end)));
			},
			_ => ans.push(None),
		}
	}
	json!(ans)
}
