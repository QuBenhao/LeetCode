use serde_json::{json, Value};


struct ExamRoom {

}


/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl ExamRoom {

    fn new(n: i32) -> Self {
        
    }
    
    fn seat(&self) -> i32 {
        
    }
    
    fn leave(&self, p: i32) {
        
    }
}

/**
 * Your ExamRoom object will be instantiated and called as such:
 * let obj = ExamRoom::new(n);
 * let ret_1: i32 = obj.seat();
 * obj.leave(p);
 */

#[cfg(feature = "solution_855")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let operators: Vec<String> = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	let op_values: Vec<Vec<Value>> = serde_json::from_str(&input_values[1]).expect("Failed to parse input");
	let n_obj: i32 = serde_json::from_value(op_values[0][0].clone()).expect("Failed to parse input");
	let mut obj = ExamRoom::new(n_obj);
	let mut ans = vec![None];
	for i in 1..operators.len() {
		match operators[i].as_str() {
			"seat" => {
				ans.push(Some(obj.seat()));
			},
			"leave" => {
				let p: i32 = serde_json::from_value(op_values[i][0].clone()).expect("Failed to parse input");
				obj.leave(p);
				ans.push(None);
			},
			_ => ans.push(None),
		}
	}
	json!(ans)
}
