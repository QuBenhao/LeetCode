use serde_json::{json, Value};

pub struct Solution;

impl Solution {
    pub fn sort_colors(nums: &mut Vec<i32>) {
        
    }
}

#[cfg(feature = "solution_75")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let mut nums: Vec<i32> = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	Solution::sort_colors(&mut nums);
	json!(nums)
}
