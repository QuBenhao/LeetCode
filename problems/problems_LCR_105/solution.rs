#![allow(non_snake_case)]
use serde_json::{json, Value};

pub struct Solution;

impl Solution {
    pub fn max_area_of_island(mut grid: Vec<Vec<i32>>) -> i32 {
        let m = grid.len();
        let n = grid[0].len();
        let mut res = 0;
		fn dfs(grid: &mut Vec<Vec<i32>>, i: usize, j: usize) -> i32 {
			if i >= grid.len() || j >= grid[0].len() || grid[i][j] == 0 {
				return 0;
			}
			grid[i][j] = 0;
			let mut res = 1;
			res += dfs(grid, i+1, j);
			res += dfs(grid, i, j+1);
			if i > 0 {
				res += dfs(grid, i-1, j);
			}
			if j > 0 {
				res += dfs(grid, i, j-1);
			}
			res
		}
		for i in 0..m {
			for j in 0..n {
				if grid[i][j] == 1 {
					res = res.max(dfs(&mut grid, i, j));
				}
			}
		}
		res
    }
}

#[cfg(feature = "solution_LCR_105")]
pub fn solve(input_string: String) -> Value {
    let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
    let grid: Vec<Vec<i32>> = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
    json!(Solution::max_area_of_island(grid))
}
