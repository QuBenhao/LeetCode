use serde_json::{json, Value};

pub struct Solution;
use std::collections::{HashMap, VecDeque};
impl Solution {
    pub fn can_finish(num_courses: i32, prerequisites: Vec<Vec<i32>>) -> bool {
		let mut degree: Vec<i32> = vec![0; num_courses as usize];
		let mut graph: HashMap<i32, Vec<i32>> = HashMap::new();
		for req in prerequisites.iter() {
			degree[req[0] as usize] += 1;
			graph.entry(req[1]).or_insert(Vec::new()).push(req[0]);
		}
		let mut queue: VecDeque<i32> = VecDeque::new();
		for i in 0..num_courses {
			if degree[i as usize] == 0 {
				queue.push_back(i);
			}
		}
		let mut count = 0;
		while !queue.is_empty() {
			let cur = queue.pop_back().unwrap();
			count += 1;
			if let Some(neighbors) = graph.get(&cur) {
				for neighbor in neighbors.iter() {
					degree[*neighbor as usize] -= 1;
					if degree[*neighbor as usize] == 0 {
						queue.push_back(*neighbor);
					}
				}
			}
		}
		count == num_courses
    }
}

#[cfg(feature = "solution_207")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let num_courses: i32 = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	let prerequisites: Vec<Vec<i32>> = serde_json::from_str(&input_values[1]).expect("Failed to parse input");
	json!(Solution::can_finish(num_courses, prerequisites))
}
