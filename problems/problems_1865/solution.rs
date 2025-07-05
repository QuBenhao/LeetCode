use serde_json::{json, Value};


struct FindSumPairs {

}


/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl FindSumPairs {

    fn new(nums1: Vec<i32>, nums2: Vec<i32>) -> Self {
        
    }
    
    fn add(&self, index: i32, val: i32) {
        
    }
    
    fn count(&self, tot: i32) -> i32 {
        
    }
}

/**
 * Your FindSumPairs object will be instantiated and called as such:
 * let obj = FindSumPairs::new(nums1, nums2);
 * obj.add(index, val);
 * let ret_2: i32 = obj.count(tot);
 */

#[cfg(feature = "solution_1865")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let operators: Vec<String> = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	let op_values: Vec<Vec<Value>> = serde_json::from_str(&input_values[1]).expect("Failed to parse input");
	let nums1_obj: Vec<i32> = serde_json::from_value(op_values[0][0].clone()).expect("Failed to parse input");
	let nums2_obj: Vec<i32> = serde_json::from_value(op_values[0][1].clone()).expect("Failed to parse input");
	let mut obj = FindSumPairs::new(nums1_obj, nums2_obj);
	let mut ans = vec![None];
	for i in 1..operators.len() {
		match operators[i].as_str() {
			"add" => {
				let index: i32 = serde_json::from_value(op_values[i][0].clone()).expect("Failed to parse input");
				let val: i32 = serde_json::from_value(op_values[i][1].clone()).expect("Failed to parse input");
				obj.add(index, val);
				ans.push(None);
			},
			"count" => {
				let tot: i32 = serde_json::from_value(op_values[i][0].clone()).expect("Failed to parse input");
				ans.push(Some(obj.count(tot)));
			},
			_ => ans.push(None),
		}
	}
	json!(ans)
}
