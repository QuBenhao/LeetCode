#![allow(non_snake_case)]
use serde_json::{json, Value};


struct WordsFrequency {

}


/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl WordsFrequency {

    fn new(book: Vec<String>) -> Self {
        
    }
    
    fn get(&self, word: String) -> i32 {
        
    }
}

/**
 * Your WordsFrequency object will be instantiated and called as such:
 * let obj = WordsFrequency::new(book);
 * let ret_1: i32 = obj.get(word);
 */

#[cfg(feature = "solution_Interview_16__02")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let operators: Vec<String> = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	let op_values: Vec<Vec<Value>> = serde_json::from_str(&input_values[1]).expect("Failed to parse input");
	let book_obj: Vec<String> = serde_json::from_value(op_values[0][0].clone()).expect("Failed to parse input");
	let mut obj = WordsFrequency::new(book_obj);
	let mut ans = vec![None];
	for i in 1..operators.len() {
		match operators[i].as_str() {
			"get" => {
				let word: String = serde_json::from_value(op_values[i][0].clone()).expect("Failed to parse input");
				ans.push(Some(obj.get(word)));
			},
			_ => ans.push(None),
		}
	}
	json!(ans)
}
