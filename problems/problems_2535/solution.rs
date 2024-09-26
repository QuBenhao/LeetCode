use serde_json::{json, Value};

pub struct Solution;

impl Solution {
    pub fn difference_of_sum(nums: Vec<i32>) -> i32 {
		let mut ans: i32 = 0;
		for num in nums {
			ans += num;
			let mut temp: i32 = num;
			while temp > 0 {
				ans -= temp % 10;
				temp /= 10;
			}
		}
		ans
    }
}

#[cfg(feature = "solution_2535")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let nums: Vec<i32> = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	json!(Solution::difference_of_sum(nums))
}
