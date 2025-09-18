use serde_json::{json, Value};


struct Spreadsheet {

}


/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl Spreadsheet {

    fn new(rows: i32) -> Self {
        
    }
    
    fn set_cell(&self, cell: String, value: i32) {
        
    }
    
    fn reset_cell(&self, cell: String) {
        
    }
    
    fn get_value(&self, formula: String) -> i32 {
        
    }
}

/**
 * Your Spreadsheet object will be instantiated and called as such:
 * let obj = Spreadsheet::new(rows);
 * obj.set_cell(cell, value);
 * obj.reset_cell(cell);
 * let ret_3: i32 = obj.get_value(formula);
 */

#[cfg(feature = "solution_3484")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let operators: Vec<String> = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	let op_values: Vec<Vec<Value>> = serde_json::from_str(&input_values[1]).expect("Failed to parse input");
	let rows_obj: i32 = serde_json::from_value(op_values[0][0].clone()).expect("Failed to parse input");
	let mut obj = Spreadsheet::new(rows_obj);
	let mut ans = vec![None];
	for i in 1..operators.len() {
		match operators[i].as_str() {
			"setCell" => {
				let cell: String = serde_json::from_value(op_values[i][0].clone()).expect("Failed to parse input");
				let value: i32 = serde_json::from_value(op_values[i][1].clone()).expect("Failed to parse input");
				obj.set_cell(cell, value);
				ans.push(None);
			},
			"resetCell" => {
				let cell: String = serde_json::from_value(op_values[i][0].clone()).expect("Failed to parse input");
				obj.reset_cell(cell);
				ans.push(None);
			},
			"getValue" => {
				let formula: String = serde_json::from_value(op_values[i][0].clone()).expect("Failed to parse input");
				ans.push(Some(obj.get_value(formula)));
			},
			_ => ans.push(None),
		}
	}
	json!(ans)
}
