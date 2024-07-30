use serde_json::{json, Value};

pub struct Solution;

impl Solution {
    fn expand(s: &[u8], mut left: usize, mut right: usize) -> (usize, usize) {
        while left > 0 && right < s.len() - 1 && s[left - 1] == s[right + 1] {
            left -= 1;
            right += 1;
        }
        (left , right)
    }
    pub fn longest_palindrome(s: String) -> String {
        let (mut start, mut end) = (0, 0);
        let bytes = s.as_bytes();
        let n = bytes.len();
        for i in 0..n {
            for j in (i..n).take(2) {
                if bytes[i] != bytes[j] {
                    continue;
                }
                let (l, r) = Self::expand(bytes, i, j);
                if r - l > end - start {
                    (start, end) = (l, r);
                }
            }
        }
        s[start..=end].to_string()
    }
}

#[cfg(feature = "solution_5")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let s: String = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	json!(Solution::longest_palindrome(s))
}
