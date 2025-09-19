use serde_json::{json, Value};


struct Router {

}


/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl Router {

    fn new(memoryLimit: i32) -> Self {
        
    }
    
    fn add_packet(&self, source: i32, destination: i32, timestamp: i32) -> bool {
        
    }
    
    fn forward_packet(&self) -> Vec<i32> {
        
    }
    
    fn get_count(&self, destination: i32, start_time: i32, end_time: i32) -> i32 {
        
    }
}

/**
 * Your Router object will be instantiated and called as such:
 * let obj = Router::new(memoryLimit);
 * let ret_1: bool = obj.add_packet(source, destination, timestamp);
 * let ret_2: Vec<i32> = obj.forward_packet();
 * let ret_3: i32 = obj.get_count(destination, startTime, endTime);
 */

#[cfg(feature = "solution_3508")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let operators: Vec<String> = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	let op_values: Vec<Vec<Value>> = serde_json::from_str(&input_values[1]).expect("Failed to parse input");
	let memoryLimit_obj: i32 = serde_json::from_value(op_values[0][0].clone()).expect("Failed to parse input");
	let mut obj = Router::new(memoryLimit_obj);
	let mut ans = vec![None];
	for i in 1..operators.len() {
		match operators[i].as_str() {
			"addPacket" => {
				let source: i32 = serde_json::from_value(op_values[i][0].clone()).expect("Failed to parse input");
				let destination: i32 = serde_json::from_value(op_values[i][1].clone()).expect("Failed to parse input");
				let timestamp: i32 = serde_json::from_value(op_values[i][2].clone()).expect("Failed to parse input");
				ans.push(Some(obj.add_packet(source, destination, timestamp)));
			},
			"forwardPacket" => {
				ans.push(Some(obj.forward_packet()));
			},
			"getCount" => {
				let destination: i32 = serde_json::from_value(op_values[i][0].clone()).expect("Failed to parse input");
				let start_time: i32 = serde_json::from_value(op_values[i][1].clone()).expect("Failed to parse input");
				let end_time: i32 = serde_json::from_value(op_values[i][2].clone()).expect("Failed to parse input");
				ans.push(Some(obj.get_count(destination, start_time, end_time)));
			},
			_ => ans.push(None),
		}
	}
	json!(ans)
}
