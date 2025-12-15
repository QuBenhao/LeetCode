use serde_json::{json, Value};

pub struct Solution;

impl Solution {
    pub fn max_profit(n: i32, present: Vec<i32>, future: Vec<i32>, hierarchy: Vec<Vec<i32>>, budget: i32) -> i32 {
        
    }
}

#[cfg(feature = "solution_3562")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let n: i32 = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	let present: Vec<i32> = serde_json::from_str(&input_values[1]).expect("Failed to parse input");
	let future: Vec<i32> = serde_json::from_str(&input_values[2]).expect("Failed to parse input");
	let hierarchy: Vec<Vec<i32>> = serde_json::from_str(&input_values[3]).expect("Failed to parse input");
	let budget: i32 = serde_json::from_str(&input_values[4]).expect("Failed to parse input");
	json!(Solution::max_profit(n, present, future, hierarchy, budget))
}
