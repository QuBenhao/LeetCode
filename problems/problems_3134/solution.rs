use serde_json::{json, Value};

pub struct Solution;

use std::collections::HashMap;
impl Solution {
    pub fn median_of_uniqueness_array(nums: Vec<i32>) -> i32 {
		let n: usize = nums.len();
		let k: i64 = ((n * (n + 1) / 2 + 1) / 2) as i64;

		let check = |x: usize| -> bool {
			let mut freq: HashMap<i32, i64> = HashMap::new();
			let mut cnt: i64 = 0;
			let mut l: usize = 0;
			for (r, &num) in nums.iter().enumerate() {
				*freq.entry(num).or_insert(0) += 1;
				while freq.len() > x {
					let num = nums[l];
					*freq.get_mut(&num).unwrap() -= 1;
					if freq[&num] == 0 {
						freq.remove(&num);
					}
					l += 1;
				}
				cnt += (r - l + 1) as i64;
				if cnt >= k {
					return true;
				}
			}
			false
		};

		let mut left: usize = 1;
		let mut right: usize = n;
		while left < right {
			let mid = left + (right - left) / 2;
			if check(mid) {
				right = mid;
			} else {
				left = mid + 1;
			}
		}
		left as i32
    }
}

#[cfg(feature = "solution_3134")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let nums: Vec<i32> = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	json!(Solution::median_of_uniqueness_array(nums))
}
