use serde_json::{json, Value};

pub struct Solution;

impl Solution {
    pub fn majority_element(nums: Vec<i32>) -> i32 {
		let mut ans = 0;
		let mut cnt = 0;
		for &num in nums.iter() {
			if cnt == 0 {
				ans = num;
				cnt = 1;
			} else {
				if num == ans {
					cnt += 1;
				} else {
					cnt -= 1;
				}
			}
		}
		ans
    }
}

#[cfg(feature = "solution_169")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let nums: Vec<i32> = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	json!(Solution::majority_element(nums))
}
