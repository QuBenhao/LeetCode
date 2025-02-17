use serde_json::{json, Value};


struct RangeFreqQuery {

}


/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl RangeFreqQuery {

    fn new(arr: Vec<i32>) -> Self {
        
    }
    
    fn query(&self, left: i32, right: i32, value: i32) -> i32 {
        
    }
}

/**
 * Your RangeFreqQuery object will be instantiated and called as such:
 * let obj = RangeFreqQuery::new(arr);
 * let ret_1: i32 = obj.query(left, right, value);
 */

#[cfg(feature = "solution_2080")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let operators: Vec<String> = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	let op_values: Vec<Vec<Value>> = serde_json::from_str(&input_values[1]).expect("Failed to parse input");
	let arr_obj: Vec<i32> = serde_json::from_value(op_values[0][0].clone()).expect("Failed to parse input");
	let mut obj = RangeFreqQuery::new(arr_obj);
	let mut ans = vec![None];
	for i in 1..operators.len() {
		match operators[i].as_str() {
			"query" => {
				let left: i32 = serde_json::from_value(op_values[i][0].clone()).expect("Failed to parse input");
				let right: i32 = serde_json::from_value(op_values[i][1].clone()).expect("Failed to parse input");
				let value: i32 = serde_json::from_value(op_values[i][2].clone()).expect("Failed to parse input");
				ans.push(Some(obj.query(left, right, value)));
			},
			_ => ans.push(None),
		}
	}
	json!(ans)
}
