use serde_json::{json, Value};


struct BookMyShow {

}


/**
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl BookMyShow {

    fn new(n: i32, m: i32) -> Self {

    }
    
    fn gather(&self, k: i32, max_row: i32) -> Vec<i32> {

    }
    
    fn scatter(&self, k: i32, max_row: i32) -> bool {

    }
}

/**
 * Your BookMyShow object will be instantiated and called as such:
 * let obj = BookMyShow::new(n, m);
 * let ret_1: Vec<i32> = obj.gather(k, maxRow);
 * let ret_2: bool = obj.scatter(k, maxRow);
 */

#[cfg(feature = "solution_2286")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let operators: Vec<String> = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	let op_values: Vec<Vec<Value>> = serde_json::from_str(&input_values[1]).expect("Failed to parse input");
	let n_obj: i32 = serde_json::from_value(op_values[0][0].clone()).expect("Failed to parse input");
	let m_obj: i32 = serde_json::from_value(op_values[0][1].clone()).expect("Failed to parse input");
	let mut obj = BookMyShow::new(n_obj, m_obj);
	let mut ans = vec![None];
	for i in 1..operators.len() {
		match operators[i].as_str() {
			"gather" => {
				let k: i32 = serde_json::from_value(op_values[i][0].clone()).expect("Failed to parse input");
				let max_row: i32 = serde_json::from_value(op_values[i][1].clone()).expect("Failed to parse input");
				ans.push(Some(obj.gather(k, max_row)));
			},
			"scatter" => {
				let k: i32 = serde_json::from_value(op_values[i][0].clone()).expect("Failed to parse input");
				let max_row: i32 = serde_json::from_value(op_values[i][1].clone()).expect("Failed to parse input");
				ans.push(Some(obj.scatter(k, max_row)));
			},
			_ => ans.push(None),
		}
	}
	json!(ans)
}
