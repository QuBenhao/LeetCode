use serde_json::{json, Value};

pub struct Solution;

impl Solution {
    pub fn busy_student(start_time: Vec<i32>, end_time: Vec<i32>, query_time: i32) -> i32 {
		let mut ans = 0;
		for i in 0..start_time.len() {
			if start_time[i] <= query_time && query_time <= end_time[i] {
				ans += 1;
			}
		}
		ans
    }
}

#[cfg(feature = "solution_1450")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let start_time: Vec<i32> = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	let end_time: Vec<i32> = serde_json::from_str(&input_values[1]).expect("Failed to parse input");
	let query_time: i32 = serde_json::from_str(&input_values[2]).expect("Failed to parse input");
	json!(Solution::busy_student(start_time, end_time, query_time))
}
