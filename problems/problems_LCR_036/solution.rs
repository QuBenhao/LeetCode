#![allow(non_snake_case)]
use serde_json::{json, Value};

pub struct Solution;

impl Solution {
    pub fn eval_rpn(tokens: Vec<String>) -> i32 {
		let mut stack: Vec<i32> = Vec::new();
		for token in tokens.iter() {
			match token.as_str() {
				"+" => {
					let a = stack.pop().unwrap();
					let b = stack.pop().unwrap();
					stack.push(b + a);
				},
				"-" => {
					let a = stack.pop().unwrap();
					let b = stack.pop().unwrap();
					stack.push(b - a);
				},
				"*" => {
					let a = stack.pop().unwrap();
					let b = stack.pop().unwrap();
					stack.push(b * a);
				},
				"/" => {
					let a = stack.pop().unwrap();
					let b = stack.pop().unwrap();
					stack.push(b / a);
				},
				_ => {
					stack.push(token.parse::<i32>().unwrap());
				},
			}
		}
		stack[0]
    }
}

#[cfg(feature = "solution_LCR_036")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let tokens: Vec<String> = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	json!(Solution::eval_rpn(tokens))
}
