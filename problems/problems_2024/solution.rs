use serde_json::{json, Value};

pub struct Solution;

impl Solution {
    pub fn max_consecutive_answers(answer_key: String, k: i32) -> i32 {
		let mut ans: i32 = 0;
		let mut count_t: i32 = 0;
		let mut left: i32 = 0;
		let chars: Vec<char> = answer_key.chars().collect();
		for right in 0..answer_key.len() as i32 {
			if chars[right as usize] == 'T' {
				count_t += 1;
			}
			while count_t > k && right - left + 1 - count_t > k {
				if chars[left as usize] == 'T' {
					count_t -= 1;
				}
				left += 1;
			}
			ans = ans.max(right - left + 1);
		}
		ans
    }
}

#[cfg(feature = "solution_2024")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let answer_key: String = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	let k: i32 = serde_json::from_str(&input_values[1]).expect("Failed to parse input");
	json!(Solution::max_consecutive_answers(answer_key, k))
}
