use serde_json::{json, Value};

pub struct Solution;

use std::collections::HashSet;

impl Solution {
    pub fn distinct_names(ideas: Vec<String>) -> i64 {
        let mut groups = vec![HashSet::new(); 26];
        for s in ideas {
            groups[(s.as_bytes()[0] - b'a') as usize].insert(s[1..].to_string()); // 按照首字母分组
        }

        let mut ans = 0i64;
        for a in 1..26 { // 枚举所有组对
            for b in 0..a {
                let m = groups[a].iter().filter(|&s| groups[b].contains(s)).count(); // 交集的大小
                ans += (groups[a].len() - m) as i64 * (groups[b].len() - m) as i64;
            }
        }
        ans * 2 // 乘 2 放到最后
    }
}

#[cfg(feature = "solution_2306")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let ideas: Vec<String> = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	json!(Solution::distinct_names(ideas))
}
