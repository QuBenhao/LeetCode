use serde_json::{json, Value};

pub struct Solution;

impl Solution {
    pub fn minimum_added_integer(nums1: Vec<i32>, nums2: Vec<i32>) -> i32 {
		let mut nums1 = nums1;
		nums1.sort_unstable();
		let mut nums2 = nums2;
		nums2.sort_unstable();
		for i in (1..3).rev() {
			let diff = nums2[0] - nums1[i];
			let mut quota = 2 - i;
			let mut idx = i + 1;
			let mut valid = true;
			for j in 1..nums2.len() {
				while nums2[j] - nums1[idx] != diff {
					if quota == 0 {
						valid = false;
						break;
					}
					quota -= 1;
					idx += 1;
				}
				if !valid {
					break;
				}
				idx += 1;
			}
			if valid {
				return diff;
			}
		}
		nums2[0] - nums1[0]
    }
}

#[cfg(feature = "solution_3132")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let nums1: Vec<i32> = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	let nums2: Vec<i32> = serde_json::from_str(&input_values[1]).expect("Failed to parse input");
	json!(Solution::minimum_added_integer(nums1, nums2))
}
