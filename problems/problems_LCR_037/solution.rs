#![allow(non_snake_case)]
use serde_json::{json, Value};

pub struct Solution;

impl Solution {
    pub fn asteroid_collision(asteroids: Vec<i32>) -> Vec<i32> {
		let mut stack: Vec<i32> = Vec::new();
		for asteroid in asteroids {
			let mut flag: bool = true;
			while !stack.is_empty() && stack.last().unwrap() > &0 && asteroid < 0 {
				if stack.last().unwrap() < &(-asteroid) {
					stack.pop();
				} else if stack.last().unwrap() == &(-asteroid) {
					stack.pop();
					flag = false;
					break;
				} else {
					flag = false;
					break;
				}
			}
			if flag {
				stack.push(asteroid);
			}
		}
		stack
    }
}

#[cfg(feature = "solution_LCR_037")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let asteroids: Vec<i32> = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	json!(Solution::asteroid_collision(asteroids))
}
