use serde_json::{json, Value};

pub struct Solution;

impl Solution {
    pub fn ways_to_reach_stair(k: i32) -> i32 {
        let mut n = 0;
        let mut npow = 1;
        let mut ans = 0;
        loop {
            if npow - n - 1 <= k && k <= npow {
                ans += Self::comb(n + 1, npow - k);
            } else if npow - n - 1 > k {
                break;
            }
            n += 1;
            npow *= 2;
        }
        ans
    }

    fn comb(n: i32, k: i32) -> i32 {
        let mut ans: i64 = 1;
        for i in (n - k + 1..=n).rev() {
            ans *= i as i64;
            ans /= (n - i + 1) as i64;
        }
        ans as i32
    }
}

#[cfg(feature = "solution_3154")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let k: i32 = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	json!(Solution::ways_to_reach_stair(k))
}
