use serde_json::{json, Value};

pub struct Solution;

impl Solution {
    pub fn shopping_offers(price: Vec<i32>, special: Vec<Vec<i32>>, needs: Vec<i32>) -> i32 {
        
    }
}

#[cfg(feature = "solution_638")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let price: Vec<i32> = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	let special: Vec<Vec<i32>> = serde_json::from_str(&input_values[1]).expect("Failed to parse input");
	let needs: Vec<i32> = serde_json::from_str(&input_values[2]).expect("Failed to parse input");
	json!(Solution::shopping_offers(price, special, needs))
}
