use serde_json::{json, Value};


struct MovieRentingSystem {

}


/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl MovieRentingSystem {

    fn new(n: i32, entries: Vec<Vec<i32>>) -> Self {
        
    }
    
    fn search(&self, movie: i32) -> Vec<i32> {
        
    }
    
    fn rent(&self, shop: i32, movie: i32) {
        
    }
    
    fn drop(&self, shop: i32, movie: i32) {
        
    }
    
    fn report(&self) -> Vec<Vec<i32>> {
        
    }
}

/**
 * Your MovieRentingSystem object will be instantiated and called as such:
 * let obj = MovieRentingSystem::new(n, entries);
 * let ret_1: Vec<i32> = obj.search(movie);
 * obj.rent(shop, movie);
 * obj.drop(shop, movie);
 * let ret_4: Vec<Vec<i32>> = obj.report();
 */

#[cfg(feature = "solution_1912")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let operators: Vec<String> = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	let op_values: Vec<Vec<Value>> = serde_json::from_str(&input_values[1]).expect("Failed to parse input");
	let n_obj: i32 = serde_json::from_value(op_values[0][0].clone()).expect("Failed to parse input");
	let entries_obj: Vec<Vec<i32>> = serde_json::from_value(op_values[0][1].clone()).expect("Failed to parse input");
	let mut obj = MovieRentingSystem::new(n_obj, entries_obj);
	let mut ans = vec![None];
	for i in 1..operators.len() {
		match operators[i].as_str() {
			"search" => {
				let movie: i32 = serde_json::from_value(op_values[i][0].clone()).expect("Failed to parse input");
				ans.push(Some(obj.search(movie)));
			},
			"rent" => {
				let shop: i32 = serde_json::from_value(op_values[i][0].clone()).expect("Failed to parse input");
				let movie: i32 = serde_json::from_value(op_values[i][1].clone()).expect("Failed to parse input");
				obj.rent(shop, movie);
				ans.push(None);
			},
			"drop" => {
				let shop: i32 = serde_json::from_value(op_values[i][0].clone()).expect("Failed to parse input");
				let movie: i32 = serde_json::from_value(op_values[i][1].clone()).expect("Failed to parse input");
				obj.drop(shop, movie);
				ans.push(None);
			},
			"report" => {
				ans.push(Some(obj.report()));
			},
			_ => ans.push(None),
		}
	}
	json!(ans)
}
