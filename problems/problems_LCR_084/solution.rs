#![allow(non_snake_case)]
use serde_json::{json, Value};

pub struct Solution;

use std::collections::HashSet;
impl Solution {
    pub fn permute_unique(nums: Vec<i32>) -> Vec<Vec<i32>> {
        fn dfs(a: &Vec<i32>, used: &mut Vec<bool>, tmp: &mut Vec<i32>, ans: &mut HashSet<Vec<i32>>) {
            if ans.get(tmp).is_some() {
                return;
            } else {
                ans.insert(tmp.clone());
            }
            for i in 0..a.len() {
                if !used[i] {
                    used[i] = true;
                    tmp.push(a[i]);
                    dfs(a, used, tmp, ans);
                    tmp.pop();
                    used[i] = false;
                }
            }
        }
        let mut ans = HashSet::with_capacity(1 << (nums.len() + 2));
        let mut used = vec![false; nums.len()];
        let mut tmp = Vec::with_capacity(nums.len());
        dfs(&nums, &mut used, &mut tmp, &mut ans);
        ans.into_iter().filter(|t| t.len() == nums.len()).collect()
    }
}

#[cfg(feature = "solution_LCR_084")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let nums: Vec<i32> = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	json!(Solution::permute_unique(nums))
}
