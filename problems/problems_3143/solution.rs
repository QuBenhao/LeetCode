use serde_json::{json, Value};

pub struct Solution;

impl Solution {
    pub fn max_points_inside_square(points: Vec<Vec<i32>>, s: String) -> i32 {
		let mut idx_map: Vec<i32> = vec![i32::MAX; 26];
		let mut dist = i32::MAX;
		for (i, c) in s.chars().enumerate() {
			let idx = (c as i32 - 'a' as i32) as usize;
			let cur = i32::max(i32::abs(points[i][0]), i32::abs(points[i][1]));
			if cur < idx_map[idx] {
				dist = dist.min(idx_map[idx]);
				idx_map[idx] = cur;
			} else {
				dist = dist.min(cur);
			}
		}
		let mut ans = 0;
		for v in idx_map {
			if v < dist {
				ans += 1;
			}
		}
		ans
    }
}

#[cfg(feature = "solution_3143")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let points: Vec<Vec<i32>> = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	let s: String = serde_json::from_str(&input_values[1]).expect("Failed to parse input");
	json!(Solution::max_points_inside_square(points, s))
}
