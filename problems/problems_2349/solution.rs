use serde_json::{json, Value};


struct NumberContainers {

}


/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl NumberContainers {

    fn new() -> Self {
        
    }
    
    fn change(&self, index: i32, number: i32) {
        
    }
    
    fn find(&self, number: i32) -> i32 {
        
    }
}

/**
 * Your NumberContainers object will be instantiated and called as such:
 * let obj = NumberContainers::new();
 * obj.change(index, number);
 * let ret_2: i32 = obj.find(number);
 */

#[cfg(feature = "solution_2349")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let operators: Vec<String> = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	let op_values: Vec<Vec<Value>> = serde_json::from_str(&input_values[1]).expect("Failed to parse input");
	let mut obj = NumberContainers::new();
	let mut ans = vec![None];
	for i in 1..operators.len() {
		match operators[i].as_str() {
			"change" => {
				let index: i32 = serde_json::from_value(op_values[i][0].clone()).expect("Failed to parse input");
				let number: i32 = serde_json::from_value(op_values[i][1].clone()).expect("Failed to parse input");
				obj.change(index, number);
				ans.push(None);
			},
			"find" => {
				let number: i32 = serde_json::from_value(op_values[i][0].clone()).expect("Failed to parse input");
				ans.push(Some(obj.find(number)));
			},
			_ => ans.push(None),
		}
	}
	json!(ans)
}
