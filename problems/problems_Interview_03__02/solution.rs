#![allow(non_snake_case)]
use serde_json::{json, Value};


struct MinStack {

}


/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl MinStack {

    /** initialize your data structure here. */
    fn new() -> Self {
        
    }
    
    fn push(&self, x: i32) {
        
    }
    
    fn pop(&self) {
        
    }
    
    fn top(&self) -> i32 {
        
    }
    
    fn get_min(&self) -> i32 {
        
    }
}

/**
 * Your MinStack object will be instantiated and called as such:
 * let obj = MinStack::new();
 * obj.push(x);
 * obj.pop();
 * let ret_3: i32 = obj.top();
 * let ret_4: i32 = obj.get_min();
 */

#[cfg(feature = "solution_Interview_03__02")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let operators: Vec<String> = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	let op_values: Vec<Vec<Value>> = serde_json::from_str(&input_values[1]).expect("Failed to parse input");
	let mut obj = MinStack::new();
	let mut ans = vec![None];
	for i in 1..operators.len() {
		match operators[i].as_str() {
			"push" => {
				let x: i32 = serde_json::from_value(op_values[i][0].clone()).expect("Failed to parse input");
				obj.push(x);
				ans.push(None);
			},
			"pop" => {
				obj.pop();
				ans.push(None);
			},
			"top" => {
				ans.push(Some(obj.top()));
			},
			"getMin" => {
				ans.push(Some(obj.get_min()));
			},
			_ => ans.push(None),
		}
	}
	json!(ans)
}
