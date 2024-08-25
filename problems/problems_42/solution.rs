use serde_json::{json, Value};

pub struct Solution;

impl Solution {
    pub fn trap(height: Vec<i32>) -> i32 {
		let n = height.len();
		let mut right_max = vec![0; n];
		for i in (0..n - 1).rev() {
			right_max[i] = right_max[i + 1].max(height[i + 1]);
		}
		let mut left_max = 0;
		let mut ans = 0;
		for i in 1..n-1 {
			left_max = left_max.max(height[i - 1]);
			let min = left_max.min(right_max[i]);
			if min > height[i] {
				ans += min - height[i];
			}
		}
		ans
    }
}

#[cfg(feature = "solution_42")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let height: Vec<i32> = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	json!(Solution::trap(height))
}
