use serde_json::{json, Value};

pub struct Solution;

impl Solution {
    pub fn can_make_square(grid: Vec<Vec<char>>) -> bool {
		let m = grid.len();
		let n = grid[0].len();
		for i in 0..m-1 {
			for j in 0..n-1 {
				let mut count = 0;
				for r in i..=i+1 {
					for c in j..=j+1 {
						if grid[r][c] == 'B' {
							count += 1;
						}
					}
				}
				if count != 2 {
					return true;
				}
			}
		}
		false
    }
}

#[cfg(feature = "solution_3127")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let grid: Vec<Vec<char>> = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	json!(Solution::can_make_square(grid))
}
