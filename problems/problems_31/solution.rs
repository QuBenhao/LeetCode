use serde_json::{json, Value};

pub struct Solution;

impl Solution {
    pub fn next_permutation(nums: &mut Vec<i32>) {
		let n: usize = nums.len();
		let mut idx: usize = n - 1;
		while idx > 0 && nums[idx - 1] >= nums[idx] {
			idx -= 1;
		}
		if idx == 0 {
			nums.reverse();
			return;
		}
		let mut i: usize = n - 1;
		while i >= idx && nums[i] <= nums[idx - 1] {
			i -= 1;
		}
		nums.swap(idx - 1, i);
		nums[idx..].reverse();
    }
}

#[cfg(feature = "solution_31")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let mut nums: Vec<i32> = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	Solution::next_permutation(&mut nums);
	json!(nums)
}
