use serde_json::{json, Value};


struct NeighborSum {

}


/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl NeighborSum {

    fn new(grid: Vec<Vec<i32>>) -> Self {
        
    }
    
    fn adjacent_sum(&self, value: i32) -> i32 {
        
    }
    
    fn diagonal_sum(&self, value: i32) -> i32 {
        
    }
}

/**
 * Your NeighborSum object will be instantiated and called as such:
 * let obj = NeighborSum::new(grid);
 * let ret_1: i32 = obj.adjacent_sum(value);
 * let ret_2: i32 = obj.diagonal_sum(value);
 */

#[cfg(feature = "solution_3242")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let operators: Vec<String> = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	let op_values: Vec<Vec<Value>> = serde_json::from_str(&input_values[1]).expect("Failed to parse input");
	let grid_obj: Vec<Vec<i32>> = serde_json::from_value(op_values[0][0].clone()).expect("Failed to parse input");
	let mut obj = NeighborSum::new(grid_obj);
	let mut ans = vec![None];
	for i in 1..operators.len() {
		match operators[i].as_str() {
			"adjacentSum" => {
				let value: i32 = serde_json::from_value(op_values[i][0].clone()).expect("Failed to parse input");
				ans.push(Some(obj.adjacent_sum(value)));
			},
			"diagonalSum" => {
				let value: i32 = serde_json::from_value(op_values[i][0].clone()).expect("Failed to parse input");
				ans.push(Some(obj.diagonal_sum(value)));
			},
			_ => ans.push(None),
		}
	}
	json!(ans)
}
