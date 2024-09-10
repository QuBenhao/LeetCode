use serde_json::{json, Value};

pub struct Solution;

impl Solution {
    pub fn count_quadruplets(nums: Vec<i32>) -> i64 {
		let mut cnt4: i64 = 0;
		let n = nums.len();
		let mut cnt3: Vec<i64> = vec![0; n];
		for l in 2..n {
			let mut cnt2: i64 = 0;
			for j in 0..l {
				if nums[j] < nums[l] {
					cnt4 += cnt3[j];
					cnt2 += 1;
				} else {
					cnt3[j] += cnt2;
				}
			}
		}
		cnt4
    }
}

#[cfg(feature = "solution_2552")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let nums: Vec<i32> = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	json!(Solution::count_quadruplets(nums))
}
