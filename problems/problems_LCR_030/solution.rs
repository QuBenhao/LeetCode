#![allow(non_snake_case)]
use serde_json::{json, Value};


struct RandomizedSet {

}


/**
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl RandomizedSet {

    /** Initialize your data structure here. */
    fn new() -> Self {

    }
    
    /** Inserts a value to the set. Returns true if the set did not already contain the specified element. */
    fn insert(&self, val: i32) -> bool {

    }
    
    /** Removes a value from the set. Returns true if the set contained the specified element. */
    fn remove(&self, val: i32) -> bool {

    }
    
    /** Get a random element from the set. */
    fn get_random(&self) -> i32 {

    }
}

/**
 * Your RandomizedSet object will be instantiated and called as such:
 * let obj = RandomizedSet::new();
 * let ret_1: bool = obj.insert(val);
 * let ret_2: bool = obj.remove(val);
 * let ret_3: i32 = obj.get_random();
 */

#[cfg(feature = "solution_LCR_030")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let operators: Vec<String> = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	let op_values: Vec<Vec<Value>> = serde_json::from_str(&input_values[1]).expect("Failed to parse input");
	let mut obj = RandomizedSet::new();
	let mut ans = vec![None];
	for i in 1..operators.len() {
		match operators[i].as_str() {
			"insert" => {
				let val: i32 = serde_json::from_value(op_values[i][0].clone()).expect("Failed to parse input");
				ans.push(Some(obj.insert(val)));
			},
			"remove" => {
				let val: i32 = serde_json::from_value(op_values[i][0].clone()).expect("Failed to parse input");
				ans.push(Some(obj.remove(val)));
			},
			"getRandom" => {
				ans.push(Some(obj.get_random()));
			},
			_ => ans.push(None),
		}
	}
	json!(ans)
}
