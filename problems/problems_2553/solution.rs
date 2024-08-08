use serde_json::{json, Value};

pub struct Solution;

impl Solution {
    pub fn separate_digits(nums: Vec<i32>) -> Vec<i32> {
		let mut ans: Vec<i32> = Vec::new();
		for mut num in nums {
			let mut cur: Vec<i32> = Vec::new();
			while num > 0 {
				cur.push(num % 10);
				num = num / 10;
			}
			cur.reverse();
			ans.append(&mut cur);
		}
		ans
    }
}

#[cfg(feature = "solution_2553")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let nums: Vec<i32> = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	json!(Solution::separate_digits(nums))
}
