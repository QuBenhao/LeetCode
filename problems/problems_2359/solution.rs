use serde_json::{json, Value};

pub struct Solution;

impl Solution {
    pub fn closest_meeting_node(edges: Vec<i32>, node1: i32, node2: i32) -> i32 {
        
    }
}

#[cfg(feature = "solution_2359")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let edges: Vec<i32> = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	let node1: i32 = serde_json::from_str(&input_values[1]).expect("Failed to parse input");
	let node2: i32 = serde_json::from_str(&input_values[2]).expect("Failed to parse input");
	json!(Solution::closest_meeting_node(edges, node1, node2))
}
