use serde_json::{json, Value};

pub struct Solution;

impl Solution {
    pub fn min_cost(start_pos: Vec<i32>, home_pos: Vec<i32>, row_costs: Vec<i32>, col_costs: Vec<i32>) -> i32 {
        
    }
}

#[cfg(feature = "solution_2087")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let start_pos: Vec<i32> = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	let home_pos: Vec<i32> = serde_json::from_str(&input_values[1]).expect("Failed to parse input");
	let row_costs: Vec<i32> = serde_json::from_str(&input_values[2]).expect("Failed to parse input");
	let col_costs: Vec<i32> = serde_json::from_str(&input_values[3]).expect("Failed to parse input");
	json!(Solution::min_cost(start_pos, home_pos, row_costs, col_costs))
}
