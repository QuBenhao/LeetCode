use serde_json::{json, Value};

pub struct Solution;

impl Solution {
    pub fn valid_strings(n: i32) -> Vec<String> {
        fn dfs(i: usize, path: &mut Vec<char>, ans: &mut Vec<String>) {
            if i == path.len() {
                ans.push(path.iter().collect());
                return;
            }

            // 填 0
            if i == 0 || path[i - 1] == '1' {
                path[i] = '0'; // 直接覆盖
                dfs(i + 1, path, ans);
            }

            // 填 1
            path[i] = '1';
            dfs(i + 1, path, ans);

        }

        let mut ans = vec![];
        let mut path = vec!['\0'; n as usize];
        dfs(0, &mut path, &mut ans);
        ans
    }
}

#[cfg(feature = "solution_3211")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let n: i32 = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	json!(Solution::valid_strings(n))
}
