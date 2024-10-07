use serde_json::{json, Value};

pub struct Solution;

use std::cmp::min;

impl Solution {
    pub fn min_cost(max_time: i32, edges: Vec<Vec<i32>>, passing_fees: Vec<i32>) -> i32 {
        let n = passing_fees.len();
        let mut f = vec![vec![i32::MAX; n]; (max_time + 1) as usize];
        f[0][0] = passing_fees[0];

        for t in 1..=max_time {
            for edge in &edges {
                let (i, j, cost) = (edge[0] as usize, edge[1] as usize, edge[2]);
                if cost <= t {
                    if f[(t - cost) as usize][j] != i32::MAX {
                        f[t as usize][i] = min(f[t as usize][i], f[(t - cost) as usize][j] + passing_fees[i]);
                    }
                    if f[(t - cost) as usize][i] != i32::MAX {
                        f[t as usize][j] = min(f[t as usize][j], f[(t - cost) as usize][i] + passing_fees[j]);
                    }
                }
            }
        }

        let mut ans = i32::MAX;
        for t in 1..=max_time {
            ans = min(ans, f[t as usize][n - 1]);
        }
        if ans == i32::MAX {
            -1
        } else {
            ans
        }
    }
}

#[cfg(feature = "solution_1928")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let max_time: i32 = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	let edges: Vec<Vec<i32>> = serde_json::from_str(&input_values[1]).expect("Failed to parse input");
	let passing_fees: Vec<i32> = serde_json::from_str(&input_values[2]).expect("Failed to parse input");
	json!(Solution::min_cost(max_time, edges, passing_fees))
}
