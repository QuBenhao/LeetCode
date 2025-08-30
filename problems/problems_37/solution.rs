use serde_json::{json, Value};

pub struct Solution;

impl Solution {
    pub fn solve_sudoku(board: &mut Vec<Vec<char>>) {
        
    }
}

#[cfg(feature = "solution_37")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let mut board: Vec<Vec<char>> = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	Solution::solve_sudoku(&mut board);
	json!(board)
}
