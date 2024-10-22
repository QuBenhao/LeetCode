use serde_json::{json, Value};

pub struct Solution;

impl Solution {
    pub fn count_complete_day_pairs(hours: Vec<i32>) -> i32 {
        let mut hs: Vec<i32> = vec![0; 24];
		let mut res: i32 = 0;
		for h in hours {
			hs[h as usize % 24usize] += 1;
		}
		for i in 1..12 {
			res += hs[i] * hs[24 - i];
		}
		res += hs[0] * (hs[0] - 1) / 2;
		res += hs[12] * (hs[12] - 1) / 2;
		res
    }
}

#[cfg(feature = "solution_3184")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let hours: Vec<i32> = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	json!(Solution::count_complete_day_pairs(hours))
}
