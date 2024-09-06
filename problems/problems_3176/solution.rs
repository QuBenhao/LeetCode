use serde_json::{json, Value};

pub struct Solution;
use std::collections::HashMap;

impl Solution {
    pub fn maximum_length(nums: Vec<i32>, k: i32) -> i32 {
        let mut dp = HashMap::new();
        let mut zd = vec![0; k as usize + 1];

        for &v in &nums {
            let tmp = dp.entry(v).or_insert(vec![0; k as usize + 1]);
            for j in 0..=k as usize {
                tmp[j] += 1;
                if j > 0 {
                    tmp[j] = tmp[j].max(zd[j - 1] + 1);
                }
            }

            for j in 0..=k as usize {
                zd[j] = zd[j].max(tmp[j]);
                if j > 0 {
                    zd[j] = zd[j].max(zd[j - 1]);
                }
            }
        }
        zd[k as usize]
    }
}

#[cfg(feature = "solution_3176")]
pub fn solve(input_string: String) -> Value {
    let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
    let nums: Vec<i32> = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
    let k: i32 = serde_json::from_str(&input_values[1]).expect("Failed to parse input");
    json!(Solution::maximum_length(nums, k))
}
