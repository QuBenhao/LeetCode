use serde_json::{json, Value};


struct SeatManager {

}


/**
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl SeatManager {

    fn new(n: i32) -> Self {

    }
    
    fn reserve(&self) -> i32 {

    }
    
    fn unreserve(&self, seat_number: i32) {

    }
}

/**
 * Your SeatManager object will be instantiated and called as such:
 * let obj = SeatManager::new(n);
 * let ret_1: i32 = obj.reserve();
 * obj.unreserve(seatNumber);
 */

#[cfg(feature = "solution_1845")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let operators: Vec<String> = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	let op_values: Vec<Vec<Value>> = serde_json::from_str(&input_values[1]).expect("Failed to parse input");
	let n_obj: i32 = serde_json::from_value(op_values[0][0].clone()).expect("Failed to parse input");
	let mut obj = SeatManager::new(n_obj);
	let mut ans = vec![None];
	for i in 1..operators.len() {
		match operators[i].as_str() {
			"reserve" => {
				ans.push(Some(obj.reserve()));
			},
			"unreserve" => {
				let seat_number: i32 = serde_json::from_value(op_values[i][0].clone()).expect("Failed to parse input");
				obj.unreserve(seat_number);
				ans.push(None);
			},
			_ => ans.push(None),
		}
	}
	json!(ans)
}
