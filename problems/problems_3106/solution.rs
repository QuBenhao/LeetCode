use serde_json::{json, Value};

pub struct Solution;

use std::cmp::min;
impl Solution {
    pub fn get_smallest_string(s: String, k: i32) -> String {
        let distance = |a: char, b: char| -> i32 {
            return min((b as i32 - a as i32 + 26) % 26, (a as i32 - b as i32 + 26) % 26);
        };
        let mut k = k;
        let mut s = s.into_bytes();
        let mut idx = 0;
        while idx < s.len() && k > 0{
			let c = s[idx] as char;
			if c != 'a' {
				let d = distance('a', c);
				if d <= k {
					s[idx] = 'a' as u8;
					k -= d;
				} else {
					s[idx] = (c as u8 - k as u8).into();
					k = 0;
				}
			}
            idx += 1;
        }
        String::from_utf8(s).expect("Failed to convert to string")
    }
}

#[cfg(feature = "solution_3106")]
pub fn solve(input_string: String) -> Value {
    let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
    let s: String = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
    let k: i32 = serde_json::from_str(&input_values[1]).expect("Failed to parse input");
    json!(Solution::get_smallest_string(s, k))
}
