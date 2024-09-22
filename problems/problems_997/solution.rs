use serde_json::{json, Value};

pub struct Solution;

impl Solution {
    pub fn find_judge(n: i32, trust: Vec<Vec<i32>>) -> i32 {
		let mut trust_count = vec![0; (n + 1) as usize];
		for t in trust.iter() {
			trust_count[t[0] as usize] -= 1;
			trust_count[t[1] as usize] += 1;
		}
		for i in 1..=n {
			if trust_count[i as usize] == n - 1 {
				return i;
			}
		}
		-1
    }
}

#[cfg(feature = "solution_997")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let n: i32 = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	let trust: Vec<Vec<i32>> = serde_json::from_str(&input_values[1]).expect("Failed to parse input");
	json!(Solution::find_judge(n, trust))
}
