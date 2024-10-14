use serde_json::{json, Value};

pub struct Solution;

impl Solution {
    pub fn super_egg_drop(k: i32, n: i32) -> i32 {
		let mut f: Vec<i32> = vec![0; k as usize + 1];
		let mut i = 1;
		loop {
			let mut j = k;
			while j > 0 {
				f[j as usize] = f[j as usize] + f[j as usize - 1] + 1;
				j -= 1;
			}
			if f[k as usize] >= n {
				break;
			}
			i += 1;
		}
		i
    }
}

#[cfg(feature = "solution_887")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let k: i32 = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	let n: i32 = serde_json::from_str(&input_values[1]).expect("Failed to parse input");
	json!(Solution::super_egg_drop(k, n))
}
