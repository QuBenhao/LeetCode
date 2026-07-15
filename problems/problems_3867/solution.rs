use serde_json::{json, Value};

pub struct Solution;

impl Solution {
    fn gcd(mut a: i32, mut b: i32) -> i32 {
        while b != 0 {
            let t = a % b;
            a = b;
            b = t;
        }
        a
    }

    pub fn gcd_sum(nums: Vec<i32>) -> i64 {
        let mut pg: Vec<i32> = nums
            .iter()
            .scan(0, |mx, &x| {
                if x > *mx {
                    *mx = x;
                }
                Some(Self::gcd(x, *mx))
            })
            .collect();
        pg.sort_unstable();
        let (mut i, mut j) = (0, pg.len() - 1);
        let mut ans: i64 = 0;
        while i < j {
            ans += Self::gcd(pg[i], pg[j]) as i64;
            i += 1;
            j -= 1;
        }
        ans
    }
}

#[cfg(feature = "solution_3867")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let nums: Vec<i32> = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	json!(Solution::gcd_sum(nums))
}
