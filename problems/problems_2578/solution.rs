use serde_json::{json, Value};

pub struct Solution;

impl Solution {
    pub fn split_num(num: i32) -> i32 {
		let mut nums: Vec<i32> = Vec::new();
		let mut num = num;
		while num > 0 {
			if num % 10 > 0 {
				nums.push(num % 10);
			}
			num = num / 10;
		}
		nums.sort_unstable();
		let mut a = 0;
		let mut b = 0;
		for v in nums {
			if a <= b {
				a = a * 10 + v;
			} else {
				b = b * 10 + v;
			}
		}
		a + b
    }
}

#[cfg(feature = "solution_2578")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let num: i32 = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	json!(Solution::split_num(num))
}
