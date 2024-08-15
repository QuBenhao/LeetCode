use serde_json::{json, Value};

pub struct Solution;

use std::i32::{MAX, MIN};
impl Solution {
    pub fn max_score(grid: Vec<Vec<i32>>) -> i32 {
        let mut ans: i32 = MIN;
        let n: usize = grid[0].len();
        let mut cols_min: Vec<i32> = vec![MAX; n];
        for row in grid {
            let mut pre_min: i32 = MAX;
            for j in 0..n {
                ans = ans.max(row[j] - pre_min.min(cols_min[j]));
                cols_min[j] = cols_min[j].min(row[j]);
                pre_min = pre_min.min(cols_min[j]);
            }
        }
        return ans;
    }
}

#[cfg(feature = "solution_3148")]
pub fn solve(input_string: String) -> Value {
    let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
    let grid: Vec<Vec<i32>> =
        serde_json::from_str(&input_values[0]).expect("Failed to parse input");
    json!(Solution::max_score(grid))
}
