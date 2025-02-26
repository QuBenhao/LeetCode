use serde_json::{json, Value};


struct TextEditor {

}


/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl TextEditor {

    fn new() -> Self {
        
    }
    
    fn add_text(&self, text: String) {
        
    }
    
    fn delete_text(&self, k: i32) -> i32 {
        
    }
    
    fn cursor_left(&self, k: i32) -> String {
        
    }
    
    fn cursor_right(&self, k: i32) -> String {
        
    }
}

/**
 * Your TextEditor object will be instantiated and called as such:
 * let obj = TextEditor::new();
 * obj.add_text(text);
 * let ret_2: i32 = obj.delete_text(k);
 * let ret_3: String = obj.cursor_left(k);
 * let ret_4: String = obj.cursor_right(k);
 */

#[cfg(feature = "solution_2296")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let operators: Vec<String> = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	let op_values: Vec<Vec<Value>> = serde_json::from_str(&input_values[1]).expect("Failed to parse input");
	let mut obj = TextEditor::new();
	let mut ans = vec![None];
	for i in 1..operators.len() {
		match operators[i].as_str() {
			"addText" => {
				let text: String = serde_json::from_value(op_values[i][0].clone()).expect("Failed to parse input");
				obj.add_text(text);
				ans.push(None);
			},
			"deleteText" => {
				let k: i32 = serde_json::from_value(op_values[i][0].clone()).expect("Failed to parse input");
				ans.push(Some(obj.delete_text(k)));
			},
			"cursorLeft" => {
				let k: i32 = serde_json::from_value(op_values[i][0].clone()).expect("Failed to parse input");
				ans.push(Some(obj.cursor_left(k)));
			},
			"cursorRight" => {
				let k: i32 = serde_json::from_value(op_values[i][0].clone()).expect("Failed to parse input");
				ans.push(Some(obj.cursor_right(k)));
			},
			_ => ans.push(None),
		}
	}
	json!(ans)
}
