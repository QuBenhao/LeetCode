use serde_json::{json, Value};

pub struct Solution;

impl Solution {
    pub fn kth_grammar(n: i32, k: i32) -> i32 {
        if n == 1 {
            return 0;
        }
        let parent = Self::kth_grammar(n - 1, (k + 1) / 2);
        return (1 - parent) ^ (k & 1);
    }
}

#[cfg(feature = "solution_779")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let n: i32 = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	let k: i32 = serde_json::from_str(&input_values[1]).expect("Failed to parse input");
	json!(Solution::kth_grammar(n, k))
}
