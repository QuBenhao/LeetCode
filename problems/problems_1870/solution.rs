use serde_json::{json, Value};

pub struct Solution;

impl Solution {
    pub fn min_speed_on_time(dist: Vec<i32>, hour: f64) -> i32 {
        let mut left = 1;
        let mut right = 1_000_000_000;
        while left < right {
            let mid = (left + right) / 2;
            let mut time = 0.0;
            for i in 0..dist.len() - 1 {
                time += (dist[i] + mid - 1) as f64 / mid as f64;
            }
            time += dist[dist.len() - 1] as f64 / mid as f64;
            if time > hour {
                left = mid + 1;
            } else {
                right = mid;
            }
        }
        if left == 1_000_000_001 {
            -1
        } else {
            left
        }
    }
}

#[cfg(feature = "solution_1870")]
pub fn solve(input_string: String) -> Value {
    let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
    let dist: Vec<i32> = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
    let hour: f64 = serde_json::from_str(&input_values[1]).expect("Failed to parse input");
    json!(Solution::min_speed_on_time(dist, hour))
}
