use serde_json::{json, Value};

pub struct Solution;

impl Solution {
    pub fn find_permutation_difference(s: String, t: String) -> i32 {
		let mut idxes: Vec<i32> = vec![0; 26];
		let mut ans: i32 = 0;
		let chars: Vec<char> = s.chars().collect();
		let chart: Vec<char> = t.chars().collect();
		for i in 0..s.len() {
			idxes[chars[i] as usize - 'a' as usize] += i as i32;
			idxes[chart[i] as usize - 'a' as usize] -= i as i32;
		}
		for i in idxes {
			ans += i.abs();
		}
		ans
    }
}

#[cfg(feature = "solution_3146")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let s: String = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	let t: String = serde_json::from_str(&input_values[1]).expect("Failed to parse input");
	json!(Solution::find_permutation_difference(s, t))
}
