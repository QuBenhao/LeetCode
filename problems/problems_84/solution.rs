use serde_json::{json, Value};

pub struct Solution;

impl Solution {
    pub fn largest_rectangle_area(heights: Vec<i32>) -> i32 {
		let mut stack: Vec<i32> = vec![-1; 1];
		let mut ans = 0;
		let mut heights = heights;
		heights.push(0);
		for i in 0..heights.len() {
			while stack.len() > 1 && heights[*stack.last().unwrap() as usize] > heights[i] {
				let h = heights[stack.pop().unwrap() as usize];
				ans = ans.max(h * (i as i32 - stack.last().unwrap() - 1));
			}
			stack.push(i as i32);
		}
		ans
    }
}

#[cfg(feature = "solution_84")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let heights: Vec<i32> = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	json!(Solution::largest_rectangle_area(heights))
}
