use serde_json::{json, Value};

pub struct Solution;

impl Solution {
    pub fn asteroids_destroyed(mass: i32, asteroids: Vec<i32>) -> bool {
        
    }
}

#[cfg(feature = "solution_2126")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let mass: i32 = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	let asteroids: Vec<i32> = serde_json::from_str(&input_values[1]).expect("Failed to parse input");
	json!(Solution::asteroids_destroyed(mass, asteroids))
}
