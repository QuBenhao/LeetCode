use serde_json::{json, Value};

pub struct Solution;

impl Solution {
    pub fn maxmium_score(cards: Vec<i32>, cnt: i32) -> i32 {
		let mut cards = cards;
		cards.sort_unstable_by(|a, b| b.cmp(a));
		let cnt = cnt as usize;
		let s: i32 = cards.iter().take(cnt).sum();
		if s % 2 == 0 {
			return s;
		}
		let cur = cards[cnt - 1];
		let replace_sum = |x: i32| -> i32 {
			for &v in cards.iter().skip(cnt) {
				if v % 2 != x % 2 {
					return s - x + v;
				}
			}
			0
		};
		let mut ans = replace_sum(cur);
		for &v in cards[..cnt - 1].iter().rev() {
			if v % 2 != cur % 2 {
				ans = ans.max(replace_sum(v));
				break;
			}
		}
		ans
    }
}

#[cfg(feature = "solution_LCP_40")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let cards: Vec<i32> = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	let cnt: i32 = serde_json::from_str(&input_values[1]).expect("Failed to parse input");
	json!(Solution::maxmium_score(cards, cnt))
}
