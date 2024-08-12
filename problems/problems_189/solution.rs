use serde_json::{json, Value};

pub struct Solution;

impl Solution {
    pub fn rotate(nums: &mut Vec<i32>, k: i32) {
		let reverse = |nums: &mut Vec<i32>, start: usize, end: usize| {
			let mut start = start;
			let mut end = end;
			while start < end {
				nums.swap(start, end);
				start += 1;
				end -= 1;
			}
		};
		let n = nums.len();
		let k = k as usize % n;
		if k == 0 {
			return;
		}
		reverse(nums, 0, n - 1);
		reverse(nums, 0, k - 1);
		reverse(nums, k, n - 1);
    }
}

#[cfg(feature = "solution_189")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let mut nums: Vec<i32> = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	let k: i32 = serde_json::from_str(&input_values[1]).expect("Failed to parse input");
	Solution::rotate(&mut nums, k);
	json!(nums)
}
