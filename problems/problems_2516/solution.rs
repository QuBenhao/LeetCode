use serde_json::{json, Value};

pub struct Solution;

impl Solution {
    pub fn take_characters(s: String, k: i32) -> i32 {
        let mut cnt = [0; 3];
        for c in s.bytes() {
            cnt[(c - b'a') as usize] += 1; // Initially, take all characters
        }
        if cnt[0] < k || cnt[1] < k || cnt[2] < k {
            return -1; // Fewer than k occurrences of a character
        }

        let mut mx = 0;
        let mut left = 0;
        let s = s.as_bytes();
        for (right, &c) in s.iter().enumerate() {
            let c = (c - b'a') as usize;
            cnt[c] -= 1; // Moving c into the window means leaving it untaken
            while cnt[c] < k { // Fewer than k occurrences of c remain outside the window
                cnt[(s[left] - b'a') as usize] += 1; // Moving s[left] out of the window means taking it
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
