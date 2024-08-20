use serde_json::{json, Value};

pub struct Solution;

impl Solution {
    pub fn min_window(s: String, t: String) -> String {
		let char_to_index = |c: char| -> usize {
			if c.is_ascii_lowercase() {
				(c as u8 - b'a') as usize
			} else {
				(c as u8 - b'A' + 26) as usize
			}
		};
		let mut t_count = [0; 52];
		let mut s_count = [0; 52];
		let mut diff = 0;
		for c in t.chars() {
			let index = char_to_index(c);
			if t_count[index] == 0 {
				diff += 1;
			}
			t_count[index] += 1;
		}
		let mut ans_left: i32 = -1;
		let mut ans_right: i32 = -1;
		let mut left: usize = 0;
		let chars: Vec<char> = s.chars().collect();
		for right in 0..s.len() {
			let index = char_to_index(chars[right]);
			s_count[index] += 1;
			if s_count[index] == t_count[index] {
				diff -= 1;
			}
			while left < right {
				let index = char_to_index(chars[left]);
				if s_count[index] > t_count[index] {
					s_count[index] -= 1;
					left += 1;
				} else {
					break;
				}
			}
			if diff == 0 && (ans_left == -1 || (right as i32 - left as i32) < ans_right - ans_left) {
				ans_left = left as i32;
				ans_right = right as i32;
			}
		}
		if ans_left == -1 {
			"".to_string()
		} else {
			s[ans_left as usize..=ans_right as usize].to_string()
		}
    }
}

#[cfg(feature = "solution_76")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let s: String = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	let t: String = serde_json::from_str(&input_values[1]).expect("Failed to parse input");
	json!(Solution::min_window(s, t))
}
