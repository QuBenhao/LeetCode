use serde_json::{json, Value};

pub struct Solution;

impl Solution {
    pub fn minimum_difference(mut nums: Vec<i32>, k: i32) -> i32 {
		let n = nums.len();
		let mut ans = (k - nums[0]).abs();
		for i in 1..n {
			ans = ans.min((k - nums[i]).abs());
			let mut j = i - 1;
			while (nums[j] | nums[i]) != nums[j] {
				nums[j] |= nums[i];
				ans = ans.min((k - nums[j]).abs());
				let nj = j.checked_sub(1);
				if nj.is_none() {
					break;
				}
				j = nj.unwrap();
			}
		}
		ans
    }
}

#[cfg(feature = "solution_3171")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let nums: Vec<i32> = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	let k: i32 = serde_json::from_str(&input_values[1]).expect("Failed to parse input");
	json!(Solution::minimum_difference(nums, k))
}
