use serde_json::{json, Value};

pub struct Solution;

impl Solution {
    pub fn find_duplicate(nums: Vec<i32>) -> i32 {
		let mut slow: usize = 0;
		let mut fast: usize = 0;
		loop {
			slow = nums[slow] as usize;
			fast = nums[nums[fast] as usize] as usize;
			if slow == fast {
				break;
			}
		}
		slow = 0;
		while slow != fast {
			slow = nums[slow] as usize;
			fast = nums[fast] as usize;
		}
		slow as _
    }
}

#[cfg(feature = "solution_287")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let nums: Vec<i32> = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	json!(Solution::find_duplicate(nums))
}
