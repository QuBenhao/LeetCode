use serde_json::{json, Value};

pub struct Solution;

impl Solution {
	fn fast_pow_mod(mut x: i32, mut n: i32, m: i32) -> i32 {
		let mut ans = 1;
		while n > 0 {
			if n & 1 == 1 {
				ans = (ans as i64 * x as i64 % m as i64) as i32;
			}
			x = (x as i64 * x as i64 % m as i64) as i32;
			n >>= 1;
		}
		ans
	}
    pub fn get_good_indices(variables: Vec<Vec<i32>>, target: i32) -> Vec<i32> {
		let mut ans = vec![];
		for i in 0..variables.len() {
			let a = variables[i][0];
			let b = variables[i][1];
			let c = variables[i][2];
			let m = variables[i][3];
			if Self::fast_pow_mod(Self::fast_pow_mod(a, b, 10), c, m) == target {
				ans.push(i as i32);
			}
		}
		ans
    }
}

#[cfg(feature = "solution_2961")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let variables: Vec<Vec<i32>> = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	let target: i32 = serde_json::from_str(&input_values[1]).expect("Failed to parse input");
	json!(Solution::get_good_indices(variables, target))
}
