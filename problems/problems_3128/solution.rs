use serde_json::{json, Value};

pub struct Solution;

impl Solution {
    pub fn number_of_right_triangles(grid: Vec<Vec<i32>>) -> i64 {
		let m: usize = grid.len();
		let n: usize = grid[0].len();
		let mut row_count: Vec<i64> = vec![0; m];
		let mut col_count: Vec<i64> = vec![0; n];
		for i in 0..m {
			for j in 0..n {
				row_count[i] += grid[i][j] as i64;
				col_count[j] += grid[i][j] as i64;
			}
		}
		let mut ans: i64 = 0;
		for i in 0..m {
			for j in 0..n {
				if grid[i][j] == 0 {
					continue;
				}
				ans += (row_count[i] - 1) * (col_count[j] - 1);
			}
		}
		ans
    }
}

#[cfg(feature = "solution_3128")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let grid: Vec<Vec<i32>> = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	json!(Solution::number_of_right_triangles(grid))
}
