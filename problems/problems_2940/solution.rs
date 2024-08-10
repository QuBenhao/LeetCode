use serde_json::{json, Value};

pub struct Solution;

use std::cmp::Reverse;
use std::collections::BinaryHeap;

impl Solution {
    pub fn leftmost_building_queries(heights: Vec<i32>, queries: Vec<Vec<i32>>) -> Vec<i32> {
        let n = heights.len();
        let qn = queries.len();
        let mut que: Vec<Vec<(i32, usize)>> = vec![vec![]; n];
        let mut ans = vec![-1; qn];

        for (qi, query) in queries.iter().enumerate() {
            let i = query[0] as usize;
            let j = query[1] as usize;
            if i < j && heights[i] < heights[j] { ans[qi] = j as i32; } else if i > j && heights[i] > heights[j] { ans[qi] = i as i32; } else if i == j { ans[qi] = i as i32; } else { que[std::cmp::max(i, j)].push((std::cmp::max(heights[i], heights[j]), qi)); }
        }

        let mut h = BinaryHeap::new();

        for i in 0..n {
            while let Some(Reverse((height, qi))) = h.peek() {
                if *height < heights[i] {
                    ans[*qi] = i as i32;
                    h.pop();
                } else { break; }
            }
            for &(height, qi) in &que[i] { h.push(Reverse((height, qi))); }
        }
        ans
    }
}

#[cfg(feature = "solution_2940")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let heights: Vec<i32> = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	let queries: Vec<Vec<i32>> = serde_json::from_str(&input_values[1]).expect("Failed to parse input");
	json!(Solution::leftmost_building_queries(heights, queries))
}
