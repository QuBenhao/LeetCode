use serde_json::{json, Value};

pub struct Solution;

use rand::random;
impl Solution {
    pub fn find_kth_largest(nums: Vec<i32>, k: i32) -> i32 {
		let pivot: i32 = nums[random::<usize>() % nums.len()];
		let mut left: Vec<i32> = Vec::new();
		let mut right: Vec<i32> = Vec::new();
		let mut equal: Vec<i32> = Vec::new();
		for num in nums {
			if num < pivot {
				left.push(num);
			} else if num > pivot {
				right.push(num);
			} else {
				equal.push(num);
			}
		}
		if right.len() >= k as usize {
			Solution::find_kth_largest(right, k)
		} else if right.len() + equal.len() >= k as usize {
			pivot
		} else {
			Solution::find_kth_largest(left, k - right.len() as i32 - equal.len() as i32)
		}
    }
}

#[cfg(feature = "solution_215")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let nums: Vec<i32> = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	let k: i32 = serde_json::from_str(&input_values[1]).expect("Failed to parse input");
	json!(Solution::find_kth_largest(nums, k))
}
