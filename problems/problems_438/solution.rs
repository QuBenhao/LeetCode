use serde_json::{json, Value};

pub struct Solution;

impl Solution {
    pub fn find_anagrams(s: String, p: String) -> Vec<i32> {
        let mut ans: Vec<i32> = Vec::new();
        let m = s.len();
        let n = p.len();
        let mut counts = vec![0; 26];
        for c in p.chars() {
            counts[c as usize - 'a' as usize] -= 1;
        }
        let mut diff = 0;
        for &v in counts.iter() {
            if v != 0 {
                diff += 1;
            }
        }
        let mut helper = |key: usize, val: i32| -> i32 {
            let before = counts[key] == 0;
            counts[key] += val;
            if before {
                1
            } else if counts[key] == 0 {
                -1
            } else {
                0
            }
        };
		let chars: Vec<char> = s.chars().collect();
        for i in 0..m {
            diff += helper(chars[i] as usize - 'a' as usize, 1);
            if i >= n - 1 {
                if diff == 0 {
                    ans.push(i as i32 - n as i32 + 1);
                }
                if let Some(index) = (i as isize).checked_sub(n as isize - 1) {
                    diff += helper(chars[index as usize] as usize - 'a' as usize, -1);
                }
            }
        }
        ans
    }
}

#[cfg(feature = "solution_438")]
pub fn solve(input_string: String) -> Value {
    let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
    let s: String = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
    let p: String = serde_json::from_str(&input_values[1]).expect("Failed to parse input");
    json!(Solution::find_anagrams(s, p))
}
