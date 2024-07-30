use serde_json::{json, Value};

pub struct Solution;

impl Solution {
    pub fn cal_points(operations: Vec<String>) -> i32 {
		let mut stack: Vec<i32> = Vec::new();
		let mut ans: i32 = 0;
		for operation in operations {
			match operation.as_str() {
				"C" => {
					ans -= stack.last().unwrap();
					stack.pop();
				},
				"D" => {
					let last = stack.last().unwrap();
					ans += last * 2;
					stack.push(last * 2);
				},
				"+" => {
					let last = stack.last().unwrap();
					let second_last = stack[stack.len() - 2];
					ans += last + second_last;
					stack.push(last + second_last);
				},
				_ => {
					stack.push(operation.parse::<i32>().unwrap());
					ans += stack.last().unwrap();
				}
			}
		}
		ans
    }
}

#[cfg(feature = "solution_682")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let operations: Vec<String> = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	json!(Solution::cal_points(operations))
}
