use serde_json::{json, Value};

pub struct Solution;

use std::collections::HashMap;

impl Solution {
    pub fn number_of_pairs(nums1: Vec<i32>, nums2: Vec<i32>, k: i32) -> i64 {
        let mut cnt = HashMap::new();
        for mut x in nums1 {
            if x % k != 0 {
                continue;
            }
            x /= k;
            let mut d = 1;
            while d * d <= x {
                if x % d == 0 {
                    *cnt.entry(d).or_insert(0) += 1;
                    if d * d < x {
                        *cnt.entry(x / d).or_insert(0) += 1;
                    }
                }
                d += 1;
            }
        }

        nums2.iter().map(|x| *cnt.get(x).unwrap_or(&0) as i64).sum()
    }
}

#[cfg(feature = "solution_3162")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let nums1: Vec<i32> = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	let nums2: Vec<i32> = serde_json::from_str(&input_values[1]).expect("Failed to parse input");
	let k: i32 = serde_json::from_str(&input_values[2]).expect("Failed to parse input");
	json!(Solution::number_of_pairs(nums1, nums2, k))
}
