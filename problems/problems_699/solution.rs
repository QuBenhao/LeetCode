use serde_json::{json, Value};

pub struct Solution;

use std::collections::{HashSet, HashMap};
use std::cmp::max;
impl Solution {
    pub fn falling_squares(positions: Vec<Vec<i32>>) -> Vec<i32> {
		let mut points: HashSet<i32> = HashSet::new();
		for pos in &positions {
			points.insert(pos[0]);
			points.insert(pos[0] + pos[1] - 1);
		}
		let mut points: Vec<i32> = points.into_iter().collect();
		points.sort();
		let mut index: HashMap<i32, i32> = HashMap::new();
		for i in 0..points.len() {
			index.insert(points[i], i as i32);
		}
		let mut ans: Vec<i32> = Vec::new();
		let mut heights: Vec<i32> = vec![0; points.len()];
		for i in 0..positions.len() {
			let left = index[&positions[i][0]] as usize;
			let right = index[&(positions[i][0] + positions[i][1] - 1)] as usize;
			let mut h = 0;
			for j in left..right + 1 {
				h = h.max(heights[j]);
			}
			h += positions[i][1];
			for j in left..right + 1 {
				heights[j] = h;
			}
			if ans.is_empty() {
				ans.push(h);
			} else {
				ans.push(max(ans[ans.len() - 1], h));
			}
		}
		ans
    }
}

#[cfg(feature = "solution_699")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let positions: Vec<Vec<i32>> = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	json!(Solution::falling_squares(positions))
}
