use serde_json::{json, Value};

pub struct Solution;

use std::collections::HashMap;

impl Solution {
    pub fn number_of_pairs(nums1: Vec<i32>, nums2: Vec<i32>, k: i32) -> i64 {
        let mut cnt1 = HashMap::new();
        for x in nums1 {
            if x % k == 0 {
                *cnt1.entry(x / k).or_insert(0) += 1;
            }
        }
        if cnt1.is_empty() {
            return 0;
        }

        let mut cnt2 = HashMap::new();
        for x in nums2 {
            *cnt2.entry(x).or_insert(0) += 1;
        }

        let mut ans = 0i64;
        let u = *cnt1.keys().max().unwrap();
        for (x, cnt) in cnt2 {
            let mut s = 0;
            for y in (x..=u).step_by(x as usize) { // 枚举 x 的倍数
                if let Some(&c) = cnt1.get(&y) {
                    s += c;
                }
            }
            ans += s as i64 * cnt as i64;
        }
        ans
    }
}

#[cfg(feature = "solution_3164")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let nums1: Vec<i32> = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	let nums2: Vec<i32> = serde_json::from_str(&input_values[1]).expect("Failed to parse input");
	let k: i32 = serde_json::from_str(&input_values[2]).expect("Failed to parse input");
	json!(Solution::number_of_pairs(nums1, nums2, k))
}
