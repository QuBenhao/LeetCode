use serde_json::{json, Value};

pub struct Solution;

impl Solution {
    pub fn number_of_points(nums: Vec<Vec<i32>>) -> i32 {
		let mut nums = nums;
		nums.sort_unstable();
		let mut ans = 0;
		let mut cur = nums[0][0] - 1;
		for v in nums {
			if v[0] > cur {
				ans += v[1] - v[0] + 1;
				cur = v[1];
			} else if v[1] > cur {
				ans += v[1] - cur;
				cur = v[1];
			}
		}
		ans
    }
}

#[cfg(feature = "solution_2848")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let nums: Vec<Vec<i32>> = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	json!(Solution::number_of_points(nums))
}
