use serde_json::{json, Value};

pub struct Solution;

use std::collections::HashMap;
impl Solution {
    pub fn minimum_seconds(nums: Vec<i32>) -> i32 {
        let n = nums.len();
        let idx_map: HashMap<i32, Vec<i32>> = nums.iter().enumerate().fold(HashMap::new(), |mut map, item| {
            let (idx, &num) = item;
            let vec = map.entry(num).or_insert(vec![]);
            vec.push(idx as i32);
            map
        });
        let mut ans: i32 = n as i32;
        for idxes in idx_map.values() {
            if idxes.len() == 1 {
                continue;
            }
            let mut cur: i32 = idxes.first().unwrap() + n as i32 - idxes.last().unwrap();
            for i in 1..idxes.len() {
                cur = cur.max(idxes[i] - idxes[i - 1]);
            }
            ans = ans.min(cur);
        }
        ans / 2
    }
}

#[cfg(feature = "solution_2808")]
pub fn solve(input_string: String) -> Value {
    let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
    let nums: Vec<i32> = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
    json!(Solution::minimum_seconds(nums))
}
