use serde_json::{json, Value};

pub struct Solution;

impl Solution {
    pub fn can_jump(nums: Vec<i32>) -> bool {
		let mut max_dis: i32 = 0;
		for i in 0..nums.len() {
			max_dis = max_dis.max(i as i32 + nums[i]);
			if max_dis >= nums.len() as i32 - 1 {
				return true;
			}
			if i as i32 >= max_dis {
				return false;
			}
		}
		false
    }
}

#[cfg(feature = "solution_55")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let nums: Vec<i32> = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	json!(Solution::can_jump(nums))
}
