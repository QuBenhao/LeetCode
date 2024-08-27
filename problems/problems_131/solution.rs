use serde_json::{json, Value};

pub struct Solution;

impl Solution {
    pub fn partition(s: String) -> Vec<Vec<String>> {
		let n = s.len();
		let mut dp = vec![vec![false; n]; n];
		let chars: Vec<char> = s.chars().collect();
		for i in 0..n {
			for j in 0..=i {
				if chars[i] == chars[j] && (i - j <= 2 || dp[j + 1][i - 1]) {
					dp[j][i] = true;
				}
			}
		}
		let mut res = vec![];
		let mut path = vec![];
		Solution::backtrack(&dp, &chars, 0, &mut path, &mut res);
		res
    }

	fn backtrack(dp: &Vec<Vec<bool>>, chars: &Vec<char>, start: usize, path: &mut Vec<String>, res: &mut Vec<Vec<String>>) {
		if start == chars.len() {
			res.push(path.clone());
			return;
		}
		for i in start..chars.len() {
			if dp[start][i] {
				path.push(chars[start..=i].iter().collect());
				Solution::backtrack(dp, chars, i + 1, path, res);
				path.pop();
			}
		}
	}
}

#[cfg(feature = "solution_131")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let s: String = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	json!(Solution::partition(s))
}
