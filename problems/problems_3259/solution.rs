use serde_json::{json, Value};

pub struct Solution;

impl Solution {
	pub fn max_energy_boost(energy_drink_a: Vec<i32>, energy_drink_b: Vec<i32>) -> i64 {
			let n = energy_drink_a.len();
			let mut d: Vec<Vec<i64>> = vec![vec![0; 2]; n + 1];
			for i in 1..=n {
					d[i][0] = d[i - 1][0] + energy_drink_a[i - 1] as i64;
					d[i][1] = d[i - 1][1] + energy_drink_b[i - 1] as i64;
					if i >= 2 {
							d[i][0] = d[i][0].max(d[i - 2][1] + energy_drink_a[i - 1] as i64);
							d[i][1] = d[i][1].max(d[i - 2][0] + energy_drink_b[i - 1] as i64);
					}
			}
			d[n][0].max(d[n][1])
	}
}

#[cfg(feature = "solution_3259")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let energy_drink_a: Vec<i32> = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	let energy_drink_b: Vec<i32> = serde_json::from_str(&input_values[1]).expect("Failed to parse input");
	json!(Solution::max_energy_boost(energy_drink_a, energy_drink_b))
}
