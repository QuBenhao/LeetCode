use serde_json::{json, Value};


struct BrowserHistory {

}


/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl BrowserHistory {

    fn new(homepage: String) -> Self {
        
    }
    
    fn visit(&self, url: String) {
        
    }
    
    fn back(&self, steps: i32) -> String {
        
    }
    
    fn forward(&self, steps: i32) -> String {
        
    }
}

/**
 * Your BrowserHistory object will be instantiated and called as such:
 * let obj = BrowserHistory::new(homepage);
 * obj.visit(url);
 * let ret_2: String = obj.back(steps);
 * let ret_3: String = obj.forward(steps);
 */

#[cfg(feature = "solution_1472")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let operators: Vec<String> = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	let op_values: Vec<Vec<Value>> = serde_json::from_str(&input_values[1]).expect("Failed to parse input");
	let homepage_obj: String = serde_json::from_value(op_values[0][0].clone()).expect("Failed to parse input");
	let mut obj = BrowserHistory::new(homepage_obj);
	let mut ans = vec![None];
	for i in 1..operators.len() {
		match operators[i].as_str() {
			"visit" => {
				let url: String = serde_json::from_value(op_values[i][0].clone()).expect("Failed to parse input");
				obj.visit(url);
				ans.push(None);
			},
			"back" => {
				let steps: i32 = serde_json::from_value(op_values[i][0].clone()).expect("Failed to parse input");
				ans.push(Some(obj.back(steps)));
			},
			"forward" => {
				let steps: i32 = serde_json::from_value(op_values[i][0].clone()).expect("Failed to parse input");
				ans.push(Some(obj.forward(steps)));
			},
			_ => ans.push(None),
		}
	}
	json!(ans)
}
