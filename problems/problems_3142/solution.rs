use serde_json::{json, Value};

pub struct Solution;

impl Solution {
    pub fn satisfies_conditions(grid: Vec<Vec<i32>>) -> bool {
		let m = grid.len();
		let n = grid[0].len();
		for j in 0..n-1 {
			if grid[0][j] == grid[0][j + 1] {
				return false;
			}
		}
		for j in 0..n {
			let v = grid[0][j];
			for i in 1..m {
				if grid[i][j] != v {
					return false;
				}
			}
		}
		true
    }
}

#[cfg(feature = "solution_3142")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let grid: Vec<Vec<i32>> = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	json!(Solution::satisfies_conditions(grid))
}
