#![allow(non_snake_case)]
use serde_json::{json, Value};

pub struct Solution;

impl Solution {
    pub fn relative_sort_array(arr1: Vec<i32>, arr2: Vec<i32>) -> Vec<i32> {
		let mx: i32 = *arr1.iter().max().unwrap();
		let mut cnt: Vec<i32> = vec![0; mx as usize + 1];
		let mut res: Vec<i32> = Vec::new();
		for &num in &arr1 {
			cnt[num as usize] += 1;
		}
		for &num in &arr2 {
			for _ in 0..cnt[num as usize] {
				res.push(num);
			}
			cnt[num as usize] = 0;
		}
		for i in 0..=mx {
			for _ in 0..cnt[i as usize] {
				res.push(i);
			}
		}
		res
    }
}

#[cfg(feature = "solution_LCR_075")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let arr1: Vec<i32> = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	let arr2: Vec<i32> = serde_json::from_str(&input_values[1]).expect("Failed to parse input");
	json!(Solution::relative_sort_array(arr1, arr2))
}
