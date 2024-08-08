use serde_json::{json, Value};

pub struct Solution;

impl Solution {
    pub fn added_integer(nums1: Vec<i32>, nums2: Vec<i32>) -> i32 {
		let mut m1: i32 = nums1[0];
		let mut m2: i32 = nums2[0];
		for v in nums1 {
			m1 = m1.min(v);
		}
		for v in nums2 {
			m2 = m2.min(v)
		}
		m2 - m1
    }
}

#[cfg(feature = "solution_3131")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let nums1: Vec<i32> = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	let nums2: Vec<i32> = serde_json::from_str(&input_values[1]).expect("Failed to parse input");
	json!(Solution::added_integer(nums1, nums2))
}
