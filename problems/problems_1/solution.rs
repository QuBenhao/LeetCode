use serde_json::{json, Value};
pub struct Solution;

use std::collections::HashMap;
impl Solution {
    pub fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
        let mut map: HashMap<i32, i32> = HashMap::new();
        for i in 0..nums.len() {
            let complement = target - nums[i];
            if map.contains_key(&complement) {
                return vec![*map.get(&complement).unwrap(), i as i32];
            }
            map.insert(nums[i], i as i32);
        }
        unreachable!()
    }
}

#[cfg(feature = "solution_1")]
pub fn solve(input_string: String) -> Value {
    let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
    let nums: Vec<i32> = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
    let target: i32 = serde_json::from_str(&input_values[1]).expect("Failed to parse input");
    json!(Solution::two_sum(nums, target))
}