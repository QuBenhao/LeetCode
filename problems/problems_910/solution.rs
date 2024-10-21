use serde_json::{json, Value};

pub struct Solution;

impl Solution {
    pub fn smallest_range_ii(mut nums: Vec<i32>, k: i32) -> i32 {
        nums.sort_unstable();
        let n = nums.len();
        let mut ans = nums[n - 1] - nums[0];
        for i in 1..n {
            let mx = (nums[i - 1] + k).max(nums[n - 1] - k);
            let mn = (nums[0] + k).min(nums[i] - k);
            ans = ans.min(mx - mn);
        }
        ans
    }
}

#[cfg(feature = "solution_910")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let nums: Vec<i32> = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	let k: i32 = serde_json::from_str(&input_values[1]).expect("Failed to parse input");
	json!(Solution::smallest_range_ii(nums, k))
}
