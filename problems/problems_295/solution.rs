use serde_json::{json, Value};


struct MedianFinder {

}


/**
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl MedianFinder {

    fn new() -> Self {

    }
    
    fn add_num(&self, num: i32) {

    }
    
    fn find_median(&self) -> f64 {

    }
}

/**
 * Your MedianFinder object will be instantiated and called as such:
 * let obj = MedianFinder::new();
 * obj.add_num(num);
 * let ret_2: f64 = obj.find_median();
 */

#[cfg(feature = "solution_295")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let operators: Vec<String> = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	let op_values: Vec<Vec<Value>> = serde_json::from_str(&input_values[1]).expect("Failed to parse input");
	let mut obj = MedianFinder::new();
	let mut ans = vec![None];
	for i in 1..operators.len() {
		match operators[i].as_str() {
			"addNum" => {
				let num: i32 = serde_json::from_value(op_values[i][0].clone()).expect("Failed to parse input");
				obj.add_num(num);
				ans.push(None);
			},
			"findMedian" => {
				ans.push(Some(obj.find_median()));
			},
			_ => ans.push(None),
		}
	}
	json!(ans)
}
