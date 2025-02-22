use serde_json::{json, Value};


struct Skiplist {

}


/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl Skiplist {

    fn new() -> Self {
        
    }
    
    fn search(&self, target: i32) -> bool {
        
    }
    
    fn add(&self, num: i32) {
        
    }
    
    fn erase(&self, num: i32) -> bool {
        
    }
}

/**
 * Your Skiplist object will be instantiated and called as such:
 * let obj = Skiplist::new();
 * let ret_1: bool = obj.search(target);
 * obj.add(num);
 * let ret_3: bool = obj.erase(num);
 */

#[cfg(feature = "solution_1206")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let operators: Vec<String> = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	let op_values: Vec<Vec<Value>> = serde_json::from_str(&input_values[1]).expect("Failed to parse input");
	let mut obj = Skiplist::new();
	let mut ans = vec![None];
	for i in 1..operators.len() {
		match operators[i].as_str() {
			"search" => {
				let target: i32 = serde_json::from_value(op_values[i][0].clone()).expect("Failed to parse input");
				ans.push(Some(obj.search(target)));
			},
			"add" => {
				let num: i32 = serde_json::from_value(op_values[i][0].clone()).expect("Failed to parse input");
				obj.add(num);
				ans.push(None);
			},
			"erase" => {
				let num: i32 = serde_json::from_value(op_values[i][0].clone()).expect("Failed to parse input");
				ans.push(Some(obj.erase(num)));
			},
			_ => ans.push(None),
		}
	}
	json!(ans)
}
