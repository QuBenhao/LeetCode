use serde_json::{json, Value};


struct MyCalendarThree {

}


/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl MyCalendarThree {

    fn new() -> Self {
        
    }
    
    fn book(&self, start_time: i32, end_time: i32) -> i32 {
        
    }
}

/**
 * Your MyCalendarThree object will be instantiated and called as such:
 * let obj = MyCalendarThree::new();
 * let ret_1: i32 = obj.book(startTime, endTime);
 */

#[cfg(feature = "solution_732")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let operators: Vec<String> = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	let op_values: Vec<Vec<Value>> = serde_json::from_str(&input_values[1]).expect("Failed to parse input");
	let mut obj = MyCalendarThree::new();
	let mut ans = vec![None];
	for i in 1..operators.len() {
		match operators[i].as_str() {
			"book" => {
				let start_time: i32 = serde_json::from_value(op_values[i][0].clone()).expect("Failed to parse input");
				let end_time: i32 = serde_json::from_value(op_values[i][1].clone()).expect("Failed to parse input");
				ans.push(Some(obj.book(start_time, end_time)));
			},
			_ => ans.push(None),
		}
	}
	json!(ans)
}
