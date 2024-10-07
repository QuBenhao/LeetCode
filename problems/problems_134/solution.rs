use serde_json::{json, Value};

pub struct Solution;

impl Solution {
    pub fn can_complete_circuit(gas: Vec<i32>, cost: Vec<i32>) -> i32 {
				let mut total_tank = 0;
				let mut curr_tank = 0;
				let mut starting_station = 0;

				for i in 0..gas.len() {
						total_tank += gas[i] - cost[i];
						curr_tank += gas[i] - cost[i];

						if curr_tank < 0 {
								starting_station = i + 1;
								curr_tank = 0;
						}
				}

				if total_tank >= 0 {
						starting_station as i32
				} else {
						-1
				}
    }
}

#[cfg(feature = "solution_134")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let gas: Vec<i32> = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	let cost: Vec<i32> = serde_json::from_str(&input_values[1]).expect("Failed to parse input");
	json!(Solution::can_complete_circuit(gas, cost))
}
