use serde_json::{json, Value};


struct Robot {

}


/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl Robot {

    fn new(width: i32, height: i32) -> Self {
        
    }
    
    fn step(&self, num: i32) {
        
    }
    
    fn get_pos(&self) -> Vec<i32> {
        
    }
    
    fn get_dir(&self) -> String {
        
    }
}

/**
 * Your Robot object will be instantiated and called as such:
 * let obj = Robot::new(width, height);
 * obj.step(num);
 * let ret_2: Vec<i32> = obj.get_pos();
 * let ret_3: String = obj.get_dir();
 */

#[cfg(feature = "solution_2069")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let operators: Vec<String> = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	let op_values: Vec<Vec<Value>> = serde_json::from_str(&input_values[1]).expect("Failed to parse input");
	let width_obj: i32 = serde_json::from_value(op_values[0][0].clone()).expect("Failed to parse input");
	let height_obj: i32 = serde_json::from_value(op_values[0][1].clone()).expect("Failed to parse input");
	let mut obj = Robot::new(width_obj, height_obj);
	let mut ans = vec![None];
	for i in 1..operators.len() {
		match operators[i].as_str() {
			"step" => {
				let num: i32 = serde_json::from_value(op_values[i][0].clone()).expect("Failed to parse input");
				obj.step(num);
				ans.push(None);
			},
			"getPos" => {
				ans.push(Some(obj.get_pos()));
			},
			"getDir" => {
				ans.push(Some(obj.get_dir()));
			},
			_ => ans.push(None),
		}
	}
	json!(ans)
}
