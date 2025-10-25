use serde_json::{json, Value};


struct Bank {

}


/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl Bank {

    fn new(balance: Vec<i64>) -> Self {
        
    }
    
    fn transfer(&self, account1: i32, account2: i32, money: i64) -> bool {
        
    }
    
    fn deposit(&self, account: i32, money: i64) -> bool {
        
    }
    
    fn withdraw(&self, account: i32, money: i64) -> bool {
        
    }
}

/**
 * Your Bank object will be instantiated and called as such:
 * let obj = Bank::new(balance);
 * let ret_1: bool = obj.transfer(account1, account2, money);
 * let ret_2: bool = obj.deposit(account, money);
 * let ret_3: bool = obj.withdraw(account, money);
 */

#[cfg(feature = "solution_2043")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let operators: Vec<String> = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	let op_values: Vec<Vec<Value>> = serde_json::from_str(&input_values[1]).expect("Failed to parse input");
	let balance_obj: Vec<i64> = serde_json::from_value(op_values[0][0].clone()).expect("Failed to parse input");
	let mut obj = Bank::new(balance_obj);
	let mut ans = vec![None];
	for i in 1..operators.len() {
		match operators[i].as_str() {
			"transfer" => {
				let account1: i32 = serde_json::from_value(op_values[i][0].clone()).expect("Failed to parse input");
				let account2: i32 = serde_json::from_value(op_values[i][1].clone()).expect("Failed to parse input");
				let money: i64 = serde_json::from_value(op_values[i][2].clone()).expect("Failed to parse input");
				ans.push(Some(obj.transfer(account1, account2, money)));
			},
			"deposit" => {
				let account: i32 = serde_json::from_value(op_values[i][0].clone()).expect("Failed to parse input");
				let money: i64 = serde_json::from_value(op_values[i][1].clone()).expect("Failed to parse input");
				ans.push(Some(obj.deposit(account, money)));
			},
			"withdraw" => {
				let account: i32 = serde_json::from_value(op_values[i][0].clone()).expect("Failed to parse input");
				let money: i64 = serde_json::from_value(op_values[i][1].clone()).expect("Failed to parse input");
				ans.push(Some(obj.withdraw(account, money)));
			},
			_ => ans.push(None),
		}
	}
	json!(ans)
}
