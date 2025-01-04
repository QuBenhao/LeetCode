use serde_json::{json, Value};


struct ATM {

}


/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl ATM {

    fn new() -> Self {
        
    }
    
    fn deposit(&self, banknotes_count: Vec<i32>) {
        
    }
    
    fn withdraw(&self, amount: i32) -> Vec<i32> {
        
    }
}

/**
 * Your ATM object will be instantiated and called as such:
 * let obj = ATM::new();
 * obj.deposit(banknotesCount);
 * let ret_2: Vec<i32> = obj.withdraw(amount);
 */

#[cfg(feature = "solution_2241")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let operators: Vec<String> = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	let op_values: Vec<Vec<Value>> = serde_json::from_str(&input_values[1]).expect("Failed to parse input");
	let mut obj = ATM::new();
	let mut ans = vec![None];
	for i in 1..operators.len() {
		match operators[i].as_str() {
			"deposit" => {
				let banknotes_count: Vec<i32> = serde_json::from_value(op_values[i][0].clone()).expect("Failed to parse input");
				obj.deposit(banknotes_count);
				ans.push(None);
			},
			"withdraw" => {
				let amount: i32 = serde_json::from_value(op_values[i][0].clone()).expect("Failed to parse input");
				ans.push(Some(obj.withdraw(amount)));
			},
			_ => ans.push(None),
		}
	}
	json!(ans)
}
