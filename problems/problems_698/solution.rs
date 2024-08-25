use serde_json::{json, Value};

pub struct Solution;

impl Solution {
    pub fn can_partition_k_subsets(nums: Vec<i32>, k: i32) -> bool {
		let sum: i32 = nums.iter().sum();
		if sum % k != 0 {
			return false;
		}
		let target = sum / k;
		for num in nums.iter() {
			if *num > target {
				return false;
			}
		}
		let n = nums.len();
		let mut dp = vec![-1; 1 << n];
		dp[0] = 0;
		for mask in 0..1<<n {
			for i in 0..n {
				if (mask >> i) & 1 != 0 {
					let before = mask ^ (1 << i);
					if dp[before] != -1 && dp[before] + nums[i] <= target {
						dp[mask] = (dp[before] + nums[i]) % target;
					}
				}
			}
		}
		dp[(1 << n) - 1] == 0
    }
}

#[cfg(feature = "solution_698")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let nums: Vec<i32> = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	let k: i32 = serde_json::from_str(&input_values[1]).expect("Failed to parse input");
	json!(Solution::can_partition_k_subsets(nums, k))
}
