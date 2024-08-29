use serde_json::{json, Value};

pub struct Solution;

impl Solution {
    pub fn jump(nums: Vec<i32>) -> i32 {
		let mut ans: i32 = 0;
		let n = nums.len();
		let mut cur: usize = 0;
		let mut nxt: usize = 0;
		while nxt + 1 < n {
			let mut tmp = nxt;
			for i in cur..=nxt {
				tmp = tmp.max(i + nums[i] as usize);
			}
			cur = nxt + 1;
			nxt = tmp;
			ans += 1;
		}
		ans
    }
}

#[cfg(feature = "solution_45")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let nums: Vec<i32> = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	json!(Solution::jump(nums))
}
