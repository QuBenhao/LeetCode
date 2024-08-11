use serde_json::{json, Value};

pub struct Solution;

impl Solution {
    pub fn max_uncrossed_lines(nums1: Vec<i32>, nums2: Vec<i32>) -> i32 {
		let m: usize = nums1.len();
		let n: usize = nums2.len();
		let mut dp: Vec<Vec<i32>> = vec![vec![0; n + 1]; m + 1];
		for i in 0..m {
			for j in 0..n {
				if nums1[i] == nums2[j] {
					dp[i + 1][j + 1] = dp[i][j] + 1;
				} else {
					dp[i+1][j+1] = dp[i][j + 1].max(dp[i + 1][j]);
				}
			}
		}
		dp[m][n]
    }
}

#[cfg(feature = "solution_1035")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let nums1: Vec<i32> = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	let nums2: Vec<i32> = serde_json::from_str(&input_values[1]).expect("Failed to parse input");
	json!(Solution::max_uncrossed_lines(nums1, nums2))
}
