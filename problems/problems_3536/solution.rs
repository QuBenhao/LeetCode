use serde_json::{json, Value};

pub struct Solution;

impl Solution {
    pub fn max_product(n: i32) -> i32 {
        let mut mx = 0;
        let mut sub = 0;
        let mut n = n;
        while n > 0 {
            let cur = n % 10;
            n /= 10;
            if cur > mx {
                sub = mx;
                mx = cur;
            } else if cur > sub {
                sub = cur;
            }
        }
        mx * sub
    }
}

#[cfg(feature = "solution_3536")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let n: i32 = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	json!(Solution::max_product(n))
}
