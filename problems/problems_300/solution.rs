use serde_json::{json, Value};

pub struct Solution;

impl Solution {
    pub fn length_of_lis(nums: Vec<i32>) -> i32 {
		let mut stack: Vec<i32> = vec![];
		for num in nums {
			if stack.is_empty() || *stack.last().unwrap() < num {
				stack.push(num);
			} else {
				let mut left = 0;
				let mut right = stack.len() - 1;
				while left < right {
					let mid = left + (right - left) / 2;
					if stack[mid as usize] < num {
						left = mid + 1;
					} else {
						right = mid;
					}
				}
				stack[right] = num;
			}
		}
		stack.len() as i32
    }
}

#[cfg(feature = "solution_300")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let nums: Vec<i32> = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	json!(Solution::length_of_lis(nums))
}
