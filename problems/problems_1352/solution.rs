use serde_json::{json, Value};


struct ProductOfNumbers {

}


/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl ProductOfNumbers {

    fn new() -> Self {
        
    }
    
    fn add(&self, num: i32) {
        
    }
    
    fn get_product(&self, k: i32) -> i32 {
        
    }
}

/**
 * Your ProductOfNumbers object will be instantiated and called as such:
 * let obj = ProductOfNumbers::new();
 * obj.add(num);
 * let ret_2: i32 = obj.get_product(k);
 */

#[cfg(feature = "solution_1352")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let operators: Vec<String> = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	let op_values: Vec<Vec<Value>> = serde_json::from_str(&input_values[1]).expect("Failed to parse input");
	let mut obj = ProductOfNumbers::new();
	let mut ans = vec![None];
	for i in 1..operators.len() {
		match operators[i].as_str() {
			"add" => {
				let num: i32 = serde_json::from_value(op_values[i][0].clone()).expect("Failed to parse input");
				obj.add(num);
				ans.push(None);
			},
			"getProduct" => {
				let k: i32 = serde_json::from_value(op_values[i][0].clone()).expect("Failed to parse input");
				ans.push(Some(obj.get_product(k)));
			},
			_ => ans.push(None),
		}
	}
	json!(ans)
}
