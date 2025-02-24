use serde_json::{json, Value};


struct Allocator {

}


/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl Allocator {

    fn new(n: i32) -> Self {
        
    }
    
    fn allocate(&self, size: i32, m_id: i32) -> i32 {
        
    }
    
    fn free_memory(&self, m_id: i32) -> i32 {
        
    }
}

/**
 * Your Allocator object will be instantiated and called as such:
 * let obj = Allocator::new(n);
 * let ret_1: i32 = obj.allocate(size, mID);
 * let ret_2: i32 = obj.free_memory(mID);
 */

#[cfg(feature = "solution_2502")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let operators: Vec<String> = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	let op_values: Vec<Vec<Value>> = serde_json::from_str(&input_values[1]).expect("Failed to parse input");
	let n_obj: i32 = serde_json::from_value(op_values[0][0].clone()).expect("Failed to parse input");
	let mut obj = Allocator::new(n_obj);
	let mut ans = vec![None];
	for i in 1..operators.len() {
		match operators[i].as_str() {
			"allocate" => {
				let size: i32 = serde_json::from_value(op_values[i][0].clone()).expect("Failed to parse input");
				let m_id: i32 = serde_json::from_value(op_values[i][1].clone()).expect("Failed to parse input");
				ans.push(Some(obj.allocate(size, m_id)));
			},
			"freeMemory" => {
				let m_id: i32 = serde_json::from_value(op_values[i][0].clone()).expect("Failed to parse input");
				ans.push(Some(obj.free_memory(m_id)));
			},
			_ => ans.push(None),
		}
	}
	json!(ans)
}
