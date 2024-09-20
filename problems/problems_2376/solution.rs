use serde_json::{json, Value};

pub struct Solution;

impl Solution {
    pub fn count_special_numbers(n: i32) -> i32 {
        fn dfs(i: usize, mask: usize, is_limit: bool, is_num: bool, s: &[u8], memo: &mut Vec<Vec<i32>>) -> i32 {
            if i == s.len() {
                return if is_num { 1 } else { 0 }; // is_num 为 true 表示得到了一个合法数字
            }
            if !is_limit && is_num && memo[i][mask] != -1 {
                return memo[i][mask]; // 之前计算过
            }
            let mut res = 0;
            if !is_num { // 可以跳过当前数位
                res = dfs(i + 1, mask, false, false, s, memo);
            }
            // 如果前面填的数字都和 n 的一样，那么这一位至多填数字 s[i]（否则就超过 n 啦）
            let up = if is_limit { s[i] - b'0' } else { 9 };
            // 枚举要填入的数字 d
            // 如果前面没有填数字，则必须从 1 开始（因为不能有前导零）
            let low = if is_num { 0 } else { 1 };
            for d in low..=up {
                if (mask >> d & 1) == 0 { // d 不在 mask 中，说明之前没有填过 d
                    res += dfs(i + 1, mask | (1 << d), is_limit && d == up, true, s, memo);
                }
            }
            if !is_limit && is_num {
                memo[i][mask] = res; // 记忆化
            }
            return res;
        }

        let s = n.to_string();
        let s = s.as_bytes();
        let mut memo = vec![vec![-1; 1 << 10]; s.len()]; // -1 表示没有计算过
        return dfs(0, 0, true, false, &s, &mut memo);
    }
}

#[cfg(feature = "solution_2376")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let n: i32 = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	json!(Solution::count_special_numbers(n))
}
