use serde_json::{json, Value};

pub struct Solution;

impl Solution {
    pub fn find_winning_player(skills: Vec<i32>, k: i32) -> i32 {
        let mut ans: usize = 0;
		let mut cur: i32 = 0;
		for i in 1..skills.len() {
			if skills[i] < skills[ans] {
				cur += 1;
			} else {
				cur = 1;
				ans = i;
			}
			if cur == k {
				break;
			}
		}
		ans as i32
    }
}

#[cfg(feature = "solution_3175")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let skills: Vec<i32> = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	let k: i32 = serde_json::from_str(&input_values[1]).expect("Failed to parse input");
	json!(Solution::find_winning_player(skills, k))
}
