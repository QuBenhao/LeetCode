use serde_json::{json, Value};

pub struct Solution;

impl Solution {
    pub fn get_min_distance(nums: Vec<i32>, target: i32, start: i32) -> i32 {
        let mut ans = i32::MAX;
        for (i, &num) in nums.iter().enumerate() {
            if num == target {
                ans = ans.min((i as i32 - start).abs());
            }
        }
        ans
    }
}

#[cfg(feature = "solution_1848")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let nums: Vec<i32> = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	let target: i32 = serde_json::from_str(&input_values[1]).expect("Failed to parse input");
	let start: i32 = serde_json::from_str(&input_values[2]).expect("Failed to parse input");
	json!(Solution::get_min_distance(nums, target, start))
}
