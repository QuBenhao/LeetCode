use serde_json::{json, Value};

pub struct Solution;

impl Solution {
    pub fn min_refuel_stops(target: i32, start_fuel: i32, stations: Vec<Vec<i32>>) -> i32 {
				let mut dp = vec![start_fuel];
				for station in stations {
						let (location, capacity) = (station[0], station[1]);
						for i in (0..dp.len()).rev() {
								if dp[i] >= location {
										if i + 1 >= dp.len() {
												dp.push(0);
										}
										dp[i + 1] = dp[i + 1].max(dp[i] + capacity);
								}
						}
				}
				for (i, &d) in dp.iter().enumerate() {
						if d >= target {
								return i as i32;
						}
				}
				-1
    }
}

#[cfg(feature = "solution_871")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let target: i32 = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	let start_fuel: i32 = serde_json::from_str(&input_values[1]).expect("Failed to parse input");
	let stations: Vec<Vec<i32>> = serde_json::from_str(&input_values[2]).expect("Failed to parse input");
	json!(Solution::min_refuel_stops(target, start_fuel, stations))
}
