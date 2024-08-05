use serde_json::{json, Value};

pub struct Solution;

impl Solution {
    pub fn maximum_robots(charge_times: Vec<i32>, running_costs: Vec<i32>, budget: i64) -> i32 {

    }
}

#[cfg(feature = "solution_2398")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let charge_times: Vec<i32> = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	let running_costs: Vec<i32> = serde_json::from_str(&input_values[1]).expect("Failed to parse input");
	let budget: i64 = serde_json::from_str(&input_values[2]).expect("Failed to parse input");
	json!(Solution::maximum_robots(charge_times, running_costs, budget))
}
