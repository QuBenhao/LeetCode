use serde_json::{json, Value};

pub struct Solution;

impl Solution {
    pub fn max_num_of_marked_indices(nums: Vec<i32>) -> i32 {
			let mut nums = nums;
			nums.sort_unstable();
			let n = nums.len();
			let mut left: usize = 0;
			for right in (n+1)/2..n {
				if nums[right] >= 2 * nums[left] {
					left += 1;
				}
			}
			(2 * left) as _
    }
}

#[cfg(feature = "solution_2576")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let nums: Vec<i32> = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	json!(Solution::max_num_of_marked_indices(nums))
}
