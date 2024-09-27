use serde_json::{json, Value};

pub struct Solution;

impl Solution {
    pub fn take_characters(s: String, k: i32) -> i32 {
        let mut cnt = [0; 3];
        for c in s.bytes() {
            cnt[(c - b'a') as usize] += 1; // 一开始，把所有字母都取走
        }
        if cnt[0] < k || cnt[1] < k || cnt[2] < k {
            return -1; // 字母个数不足 k
        }

        let mut mx = 0;
        let mut left = 0;
        let s = s.as_bytes();
        for (right, &c) in s.iter().enumerate() {
            let c = (c - b'a') as usize;
            cnt[c] -= 1; // 移入窗口，相当于不取走 c
            while cnt[c] < k { // 窗口之外的 c 不足 k
                cnt[(s[left] - b'a') as usize] += 1; // 移出窗口，相当于取走 s[left]
                left += 1;
            }
            mx = mx.max(right - left + 1);
        }
        (s.len() - mx) as _
    }
}

#[cfg(feature = "solution_2516")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let s: String = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	let k: i32 = serde_json::from_str(&input_values[1]).expect("Failed to parse input");
	json!(Solution::take_characters(s, k))
}
