use serde_json::{json, Value};

pub struct Solution;
use std::cmp::min;
impl Solution {
    pub fn largest1_bordered_square(grid: Vec<Vec<i32>>) -> i32 {
		let m: usize = grid.len();
		let n: usize = grid[0].len();
		let mut pre_row: Vec<Vec<i32>> = vec![vec![0; n + 1]; m];
		let mut pre_col: Vec<Vec<i32>> = vec![vec![0; m + 1]; n];
		for i in 0..m {
			for j in 0..n {
				pre_row[i][j + 1] = pre_row[i][j] + grid[i][j];
				pre_col[j][i + 1] = pre_col[j][i] + grid[i][j];
			}
		}
		for d in (1..=min(m, n)).rev() {
			for i in 0..m - d + 1 {
				for j in 0..n - d + 1 {
					if pre_row[i][j + d] - pre_row[i][j] == d as i32
						&& pre_row[i + d - 1][j + d] - pre_row[i + d - 1][j] == d as i32
						&& pre_col[j][i + d] - pre_col[j][i] == d as i32
						&& pre_col[j + d - 1][i + d] - pre_col[j + d - 1][i] == d as i32
					{
						return d as i32 * d as i32;
					}
				}
			}
		}
		0
    }
}

#[cfg(feature = "solution_1139")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let grid: Vec<Vec<i32>> = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	json!(Solution::largest1_bordered_square(grid))
}
