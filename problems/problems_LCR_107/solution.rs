#![allow(non_snake_case)]
use serde_json::{json, Value};

pub struct Solution;

impl Solution {
    pub fn update_matrix(mat: Vec<Vec<i32>>) -> Vec<Vec<i32>> {
		let m = mat.len();
		let n = mat[0].len();
		let mut ans = vec![vec![0x3f3f3f3f; n]; m];
		for i in 0..m {
			for j in 0..n {
				if mat[i][j] == 0 {
					ans[i][j] = 0;
				} else {
					if i > 0 {
						ans[i][j] = ans[i][j].min(ans[i - 1][j] + 1);
					}
					if j > 0 {
						ans[i][j] = ans[i][j].min(ans[i][j - 1] + 1);
					}
				}
			}
		}
		for i in (0..m).rev() {
			for j in (0..n).rev() {
				if i + 1 < m {
					ans[i][j] = ans[i][j].min(ans[i + 1][j] + 1);
				}
				if j + 1 < n {
					ans[i][j] = ans[i][j].min(ans[i][j + 1] + 1);
				}
			}
		}
		ans
    }
}

#[cfg(feature = "solution_LCR_107")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let mat: Vec<Vec<i32>> = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	json!(Solution::update_matrix(mat))
}
