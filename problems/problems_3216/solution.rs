use serde_json::{json, Value};

pub struct Solution;

impl Solution {
	pub fn get_smallest_string(s: String) -> String {
			let mut arr: Vec<char> = s.chars().collect();
			for i in 0..arr.len() - 1 {
					if arr[i] > arr[i + 1] && (arr[i] as u32) % 2 == (arr[i + 1] as u32) % 2 {
							arr.swap(i, i + 1);
							break;
					}
			}
			arr.iter().collect()
	}
}

#[cfg(feature = "solution_3216")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let s: String = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	json!(Solution::get_smallest_string(s))
}
