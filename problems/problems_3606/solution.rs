use serde_json::{json, Value};

pub struct Solution;

impl Solution {
    pub fn validate_coupons(code: Vec<String>, business_line: Vec<String>, is_active: Vec<bool>) -> Vec<String> {
        
    }
}

#[cfg(feature = "solution_3606")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let code: Vec<String> = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	let business_line: Vec<String> = serde_json::from_str(&input_values[1]).expect("Failed to parse input");
	let is_active: Vec<bool> = serde_json::from_str(&input_values[2]).expect("Failed to parse input");
	json!(Solution::validate_coupons(code, business_line, is_active))
}
