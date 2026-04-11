use serde_json::{json, Value};

pub struct Solution;

impl Solution {
    pub fn minimum_distance(nums: Vec<i32>) -> i32 {
        use std::collections::HashMap;
        let mut ans = i32::MAX;
        let mut record: HashMap<i32, Vec<usize>> = HashMap::new();
        for (k, &num) in nums.iter().enumerate() {
            record.entry(num).or_insert_with(Vec::new).push(k);
            if let Some(indices) = record.get(&num) {
                if indices.len() > 2 {
                    let i = indices[indices.len() - 3];
                    ans = ans.min(((k - i) * 2) as i32);
                }
            }
        }
        if ans == i32::MAX { -1 } else { ans }
    }
}

#[cfg(feature = "solution_3740")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let nums: Vec<i32> = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	json!(Solution::minimum_distance(nums))
}
