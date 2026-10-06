use serde_json::{json, Value};

pub struct Solution;

impl Solution {
    pub fn count_special_numbers(n: i32) -> i32 {
        fn dfs(i: usize, mask: usize, is_limit: bool, is_num: bool, s: &[u8], memo: &mut Vec<Vec<i32>>) -> i32 {
            if i == s.len() {
                return if is_num { 1 } else { 0 }; // is_num being true means a valid number has been formed
            }
            if !is_limit && is_num && memo[i][mask] != -1 {
                return memo[i][mask]; // Already computed
            }
            let mut res = 0;
            if !is_num { // The current digit can be skipped
                res = dfs(i + 1, mask, false, false, s, memo);
            }
            // If all previous digits match n, this digit can be at most s[i] (otherwise the number would exceed n)
            let up = if is_limit { s[i] - b'0' } else { 9 };
            // Enumerate the digit d to place
            // If no digit has been placed, start at 1 to avoid leading zeros
            let low = if is_num { 0 } else { 1 };
            for d in low..=up {
                if (mask >> d & 1) == 0 { // If d is absent from mask, it has not been used before
                    res += dfs(i + 1, mask | (1 << d), is_limit && d == up, true, s, memo);
                }
            }
            if !is_limit && is_num {
                memo[i][mask] = res; // Memoization
            }
            return res;
        }

        let s = n.to_string();
        let s = s.as_bytes();
        let mut memo = vec![vec![-1; 1 << 10]; s.len()]; // -1 means not yet computed
        return dfs(0, 0, true, false, &s, &mut memo);
    }
}

#[cfg(feature = "solution_2376")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let n: i32 = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	json!(Solution::count_special_numbers(n))
}
