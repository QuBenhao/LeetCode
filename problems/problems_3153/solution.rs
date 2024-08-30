use serde_json::{json, Value};

pub struct Solution;

impl Solution {
    pub fn sum_digit_differences(nums: Vec<i32>) -> i64 {
		let mut ans: i64 = 0;
		let mut length: usize = 0;
		let mut num: i32 = nums[0];
		while num > 0 {
			num = num / 10;
			length += 1;
		}
		let mut counter: Vec<Vec<i64>> = vec![vec![0; 10]; length];
		for i in 0..nums.len() {
			num = nums[i];
			for j in 0..length {
				let d: usize = num as usize % 10;
				ans += i as i64 - counter[j][d] as i64;
				counter[j][d] += 1;
				num = num / 10;
			}
		}
		ans
    }
}

#[cfg(feature = "solution_3153")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let nums: Vec<i32> = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	json!(Solution::sum_digit_differences(nums))
}
