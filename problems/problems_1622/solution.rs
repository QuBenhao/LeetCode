use serde_json::{json, Value};


struct Fancy {

}


/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl Fancy {

    fn new() -> Self {
        
    }
    
    fn append(&self, val: i32) {
        
    }
    
    fn add_all(&self, inc: i32) {
        
    }
    
    fn mult_all(&self, m: i32) {
        
    }
    
    fn get_index(&self, idx: i32) -> i32 {
        
    }
}

/**
 * Your Fancy object will be instantiated and called as such:
 * let obj = Fancy::new();
 * obj.append(val);
 * obj.add_all(inc);
 * obj.mult_all(m);
 * let ret_4: i32 = obj.get_index(idx);
 */

#[cfg(feature = "solution_1622")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let operators: Vec<String> = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	let op_values: Vec<Vec<Value>> = serde_json::from_str(&input_values[1]).expect("Failed to parse input");
	let mut obj = Fancy::new();
	let mut ans = vec![None];
	for i in 1..operators.len() {
		match operators[i].as_str() {
			"append" => {
				let val: i32 = serde_json::from_value(op_values[i][0].clone()).expect("Failed to parse input");
				obj.append(val);
				ans.push(None);
			},
			"addAll" => {
				let inc: i32 = serde_json::from_value(op_values[i][0].clone()).expect("Failed to parse input");
				obj.add_all(inc);
				ans.push(None);
			},
			"multAll" => {
				let m: i32 = serde_json::from_value(op_values[i][0].clone()).expect("Failed to parse input");
				obj.mult_all(m);
				ans.push(None);
			},
			"getIndex" => {
				let idx: i32 = serde_json::from_value(op_values[i][0].clone()).expect("Failed to parse input");
				ans.push(Some(obj.get_index(idx)));
			},
			_ => ans.push(None),
		}
	}
	json!(ans)
}
