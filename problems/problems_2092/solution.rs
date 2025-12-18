use serde_json::{json, Value};

pub struct Solution;

impl Solution {
    pub fn find_all_people(n: i32, meetings: Vec<Vec<i32>>, first_person: i32) -> Vec<i32> {
        
    }
}

#[cfg(feature = "solution_2092")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let n: i32 = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	let meetings: Vec<Vec<i32>> = serde_json::from_str(&input_values[1]).expect("Failed to parse input");
	let first_person: i32 = serde_json::from_str(&input_values[2]).expect("Failed to parse input");
	json!(Solution::find_all_people(n, meetings, first_person))
}
