use serde_json::{json, Value};


struct TaskManager {

}


/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl TaskManager {

    fn new(tasks: Vec<Vec<i32>>) -> Self {
        
    }
    
    fn add(&self, user_id: i32, task_id: i32, priority: i32) {
        
    }
    
    fn edit(&self, task_id: i32, new_priority: i32) {
        
    }
    
    fn rmv(&self, task_id: i32) {
        
    }
    
    fn exec_top(&self) -> i32 {
        
    }
}

/**
 * Your TaskManager object will be instantiated and called as such:
 * let obj = TaskManager::new(tasks);
 * obj.add(userId, taskId, priority);
 * obj.edit(taskId, newPriority);
 * obj.rmv(taskId);
 * let ret_4: i32 = obj.exec_top();
 */

#[cfg(feature = "solution_3408")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let operators: Vec<String> = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	let op_values: Vec<Vec<Value>> = serde_json::from_str(&input_values[1]).expect("Failed to parse input");
	let tasks_obj: Vec<Vec<i32>> = serde_json::from_value(op_values[0][0].clone()).expect("Failed to parse input");
	let mut obj = TaskManager::new(tasks_obj);
	let mut ans = vec![None];
	for i in 1..operators.len() {
		match operators[i].as_str() {
			"add" => {
				let user_id: i32 = serde_json::from_value(op_values[i][0].clone()).expect("Failed to parse input");
				let task_id: i32 = serde_json::from_value(op_values[i][1].clone()).expect("Failed to parse input");
				let priority: i32 = serde_json::from_value(op_values[i][2].clone()).expect("Failed to parse input");
				obj.add(user_id, task_id, priority);
				ans.push(None);
			},
			"edit" => {
				let task_id: i32 = serde_json::from_value(op_values[i][0].clone()).expect("Failed to parse input");
				let new_priority: i32 = serde_json::from_value(op_values[i][1].clone()).expect("Failed to parse input");
				obj.edit(task_id, new_priority);
				ans.push(None);
			},
			"rmv" => {
				let task_id: i32 = serde_json::from_value(op_values[i][0].clone()).expect("Failed to parse input");
				obj.rmv(task_id);
				ans.push(None);
			},
			"execTop" => {
				ans.push(Some(obj.exec_top()));
			},
			_ => ans.push(None),
		}
	}
	json!(ans)
}
