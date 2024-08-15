use serde_json::{json, Value};

pub struct Solution;
impl Solution {
    pub fn daily_temperatures(temperatures: Vec<i32>) -> Vec<i32> {
        let n: usize = temperatures.len();
        let mut ans: Vec<i32> = vec![0; n];
        let mut s: Vec<usize> = Vec::new();
        for i in 0..n {
            while !s.is_empty() && temperatures[*s.last().unwrap()] < temperatures[i] {
                let prev = s.pop().unwrap();
                ans[prev] = (i - prev) as i32;
            }
            s.push(i);
        }
        ans
    }
}

#[cfg(feature = "solution_739")]
pub fn solve(input_string: String) -> Value {
    let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
    let temperatures: Vec<i32> =
        serde_json::from_str(&input_values[0]).expect("Failed to parse input");
    json!(Solution::daily_temperatures(temperatures))
}
