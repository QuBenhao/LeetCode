#![allow(non_snake_case)]
use serde_json::{json, Value};


struct MapSum {

}


/**
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl MapSum {

    /** Initialize your data structure here. */
    fn new() -> Self {

    }
    
    fn insert(&self, key: String, val: i32) {

    }
    
    fn sum(&self, prefix: String) -> i32 {

    }
}

/**
 * Your MapSum object will be instantiated and called as such:
 * let obj = MapSum::new();
 * obj.insert(key, val);
 * let ret_2: i32 = obj.sum(prefix);
 */

#[cfg(feature = "solution_LCR_066")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let operators: Vec<String> = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	let op_values: Vec<Vec<Value>> = serde_json::from_str(&input_values[1]).expect("Failed to parse input");
	let mut obj = MapSum::new();
	let mut ans = vec![None];
	for i in 1..operators.len() {
		match operators[i].as_str() {
			"insert" => {
				let key: String = serde_json::from_value(op_values[i][0].clone()).expect("Failed to parse input");
				let val: i32 = serde_json::from_value(op_values[i][1].clone()).expect("Failed to parse input");
				obj.insert(key, val);
				ans.push(None);
			},
			"sum" => {
				let prefix: String = serde_json::from_value(op_values[i][0].clone()).expect("Failed to parse input");
				ans.push(Some(obj.sum(prefix)));
			},
			_ => ans.push(None),
		}
	}
	json!(ans)
}
