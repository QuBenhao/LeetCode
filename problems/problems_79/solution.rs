use serde_json::{json, Value};

pub struct Solution;

impl Solution {
    pub fn exist(board: Vec<Vec<char>>, word: String) -> bool {
        let mut board = board;
        let word = word.as_bytes();
        let m = board.len();
        let n = board[0].len();
        let directions = vec![(0, 1), (0, -1), (1, 0), (-1, 0)];
        fn backtrack(board: &mut Vec<Vec<char>>, word: &[u8], directions: &Vec<(i32, i32)>
                     , i: usize, j: usize, k: usize) -> bool {
            if i >= board.len() || j >= board[0].len() || board[i][j] != word[k] as char {
                return false;
            }
            if k == word.len() - 1 {
                return true;
            }
            let tmp = board[i][j];
            board[i][j] = ' ';
            for &(dx, dy) in directions {
				let x = i as i32 + dx;
				let y = j as i32 + dy;
				if backtrack(board, word, directions, x as usize, y as usize, k + 1) {
					return true;
				}
			}
            board[i][j] = tmp;
            false
        }
		for i in 0..m {
			for j in 0..n {
				if backtrack(&mut board, word, &directions, i, j, 0) {
					return true;
				}
			}
		}
        false
    }
}

#[cfg(feature = "solution_79")]
pub fn solve(input_string: String) -> Value {
    let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
    let board: Vec<Vec<char>> = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
    let word: String = serde_json::from_str(&input_values[1]).expect("Failed to parse input");
    json!(Solution::exist(board, word))
}
