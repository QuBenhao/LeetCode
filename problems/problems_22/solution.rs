use serde_json::{json, Value};

pub struct Solution;

impl Solution {
    pub fn generate_parenthesis(n: i32) -> Vec<String> {
		let mut ans: Vec<String> = Vec::new();
		let mut s: String = String::new();
		Solution::backtrack(&mut ans, n, &mut s, 0, 0);
		ans
    }

	fn backtrack(ans: &mut Vec<String>, n: i32, s: &mut String, left: i32, right: i32) {
		if left == n && right == n {
			ans.push(s.clone());
			return;
		}
		if left < n {
			s.push('(');
			Solution::backtrack(ans, n, s, left + 1, right);
			s.pop();
		}
		if right < left {
			s.push(')');
			Solution::backtrack(ans, n, s, left, right + 1);
			s.pop();
		}
	}
}

#[cfg(feature = "solution_22")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let n: i32 = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	json!(Solution::generate_parenthesis(n))
}
