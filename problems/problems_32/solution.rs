use serde_json::{json, Value};

pub struct Solution;

impl Solution {
    pub fn longest_valid_parentheses(s: String) -> i32 {
        let mut stack: Vec<i32> = Vec::new();
        let mut ans: i32 = 0;
        let chars: Vec<char> = s.chars().collect();
        for i in 0..s.len() {
            if chars[i] == '(' {
                stack.push(i as i32);
            } else {
                if !stack.is_empty() && chars[stack[stack.len() - 1] as usize] == '(' {
                    stack.pop();
                    ans = ans.max(i as i32 - if stack.is_empty() { -1 } else { stack[stack.len() - 1] });
                } else {
                    stack.push(i as i32);
                }
            }
        }
        ans
    }
}

#[cfg(feature = "solution_32")]
pub fn solve(input_string: String) -> Value {
    let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
    let s: String = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
    json!(Solution::longest_valid_parentheses(s))
}
