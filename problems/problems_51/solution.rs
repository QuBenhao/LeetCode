use serde_json::{json, Value};

pub struct Solution;

impl Solution {
    pub fn solve_n_queens(n: i32) -> Vec<Vec<String>> {
		let mut result: Vec<Vec<String>> = Vec::new();
		let mut board: Vec<Vec<char>> = vec![vec!['.'; n as usize]; n as usize];
		let mut col: Vec<bool> = vec![false; n as usize];
		let mut diag1: Vec<bool> = vec![false; 2 * n as usize];
		let mut diag2: Vec<bool> = vec![false; 2 * n as usize];
		fn backtrack(
			result: &mut Vec<Vec<String>>,
			board: &mut Vec<Vec<char>>,
			col: &mut Vec<bool>,
			diag1: &mut Vec<bool>,
			diag2: &mut Vec<bool>,
			row: i32,
			n: i32,
		) {
			if row == n {
				let mut board_str: Vec<String> = Vec::new();
				for i in 0..n {
					board_str.push(board[i as usize].iter().collect());
				}
				result.push(board_str);
				return;
			}
			for c in 0..n as usize {
				let idx1 = (row + c as i32) as usize;
				let idx2 = (n - 1 + row - c as i32) as usize;
				if col[c] || diag1[idx1] || diag2[idx2] {
					continue;
				}
				col[c] = true;
				diag1[idx1] = true;
				diag2[idx2] = true;
				board[row as usize][c] = 'Q';
				backtrack(result, board, col, diag1, diag2, row + 1, n);
				board[row as usize][c] = '.';
				col[c] = false;
				diag1[idx1] = false;
				diag2[idx2] = false;
			}
		}
		backtrack(&mut result, &mut board, &mut col, &mut diag1, &mut diag2, 0, n);
		result
    }
}

#[cfg(feature = "solution_51")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let n: i32 = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	json!(Solution::solve_n_queens(n))
}
