use serde_json::{json, Value};

pub struct Solution;

impl Solution {
    pub fn check_record(n: i32) -> i32 {
		const MOD: i32 = 1_000_000_007;
		let mut last_a = 1;
		let mut last_al = 0;
		let mut last_all = 0;
		let mut last = 1;
		let mut last_l = 1;
		let mut last_ll = 0;
		for _ in 1..=n {
			let al = last_a;
			let all = last_al;
			let lt = ((last + last_l) % MOD + last_ll) % MOD;
			let a = (((last_a + last_al) % MOD + last_all) % MOD + lt) % MOD;
			let l = last;
			let ll = last_l;
			last_a = a;
			last_al = al;
			last_all = all;
			last = lt;
			last_l = l;
			last_ll = ll;
		}
		last_a
    }
}

#[cfg(feature = "solution_552")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let n: i32 = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	json!(Solution::check_record(n))
}
