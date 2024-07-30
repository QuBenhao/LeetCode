use serde_json::{json, Value};

pub struct Solution;

impl Solution {
    pub fn min_rectangles_to_cover_points(points: Vec<Vec<i32>>, w: i32) -> i32 {
        let mut points = points;
        points.sort();
        let mut res = 0;
        let mut i = 0;
        while i < points.len() {
            res += 1;
			let cur = points[i][0] + w;
			while i < points.len() && points[i][0] <= cur {
				i += 1;
			}
        }
        res
    }
}

#[cfg(feature = "solution_3111")]
pub fn solve(input_string: String) -> Value {
    let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
    let points: Vec<Vec<i32>> = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
    let w: i32 = serde_json::from_str(&input_values[1]).expect("Failed to parse input");
    json!(Solution::min_rectangles_to_cover_points(points, w))
}
