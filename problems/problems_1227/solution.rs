use serde_json::{json, Value};

pub struct Solution;

impl Solution {
    pub fn nth_person_gets_nth_seat(n: i32) -> f64 {
				if n == 1 {
						return 1.0;
				}
				0.5
    }
}

#[cfg(feature = "solution_1227")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let n: i32 = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	json!(Solution::nth_person_gets_nth_seat(n))
}
