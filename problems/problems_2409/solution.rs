use serde_json::{json, Value};

pub struct Solution;

impl Solution {
    pub fn count_days_together(arrive_alice: String, leave_alice: String, arrive_bob: String, leave_bob: String) -> i32 {
        
    }
}

#[cfg(feature = "solution_2409")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let arrive_alice: String = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	let leave_alice: String = serde_json::from_str(&input_values[1]).expect("Failed to parse input");
	let arrive_bob: String = serde_json::from_str(&input_values[2]).expect("Failed to parse input");
	let leave_bob: String = serde_json::from_str(&input_values[3]).expect("Failed to parse input");
	json!(Solution::count_days_together(arrive_alice, leave_alice, arrive_bob, leave_bob))
}
