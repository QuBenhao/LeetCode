#![allow(non_snake_case)]
use serde_json::{json, Value};


struct LRUCache {

}


/**
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl LRUCache {

    fn new(capacity: i32) -> Self {

    }
    
    fn get(&self, key: i32) -> i32 {

    }
    
    fn put(&self, key: i32, value: i32) {

    }
}

/**
 * Your LRUCache object will be instantiated and called as such:
 * let obj = LRUCache::new(capacity);
 * let ret_1: i32 = obj.get(key);
 * obj.put(key, value);
 */

#[cfg(feature = "solution_LCR_031")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let operators: Vec<String> = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	let op_values: Vec<Vec<Value>> = serde_json::from_str(&input_values[1]).expect("Failed to parse input");
	let capacity_obj: i32 = serde_json::from_value(op_values[0][0].clone()).expect("Failed to parse input");
	let mut obj = LRUCache::new(capacity_obj);
	let mut ans = vec![None];
	for i in 1..operators.len() {
		match operators[i].as_str() {
			"get" => {
				let key: i32 = serde_json::from_value(op_values[i][0].clone()).expect("Failed to parse input");
				ans.push(Some(obj.get(key)));
			},
			"put" => {
				let key: i32 = serde_json::from_value(op_values[i][0].clone()).expect("Failed to parse input");
				let value: i32 = serde_json::from_value(op_values[i][1].clone()).expect("Failed to parse input");
				obj.put(key, value);
				ans.push(None);
			},
			_ => ans.push(None),
		}
	}
	json!(ans)
}
