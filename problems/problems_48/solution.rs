use serde_json::{json, Value};

pub struct Solution;

impl Solution {
    pub fn rotate(matrix: &mut Vec<Vec<i32>>) {
		let n = matrix.len();
		for i in 0..n/2 {
			for j in 0..(n + 1)/2 {
				let temp = matrix[i][j];
				matrix[i][j] = matrix[n - 1 - j][i];
				matrix[n - 1 - j][i] = matrix[n - 1 - i][n - 1 - j];
				matrix[n - 1 - i][n - 1 - j] = matrix[j][n - 1 - i];
				matrix[j][n - 1 - i] = temp;
			}
		}
    }
}

#[cfg(feature = "solution_48")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let mut matrix: Vec<Vec<i32>> = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	Solution::rotate(&mut matrix);
	json!(matrix)
}
