use serde_json::{json, Value};

pub struct Solution;

impl Solution {
    pub fn num_buses_to_destination(routes: Vec<Vec<i32>>, source: i32, target: i32) -> i32 {
		if source == target {
			return 0;
		}
		let mut stop_to_buses = std::collections::HashMap::new();
		for (bus, stops) in routes.iter().enumerate() {
			for &stop in stops {
				stop_to_buses.entry(stop).or_insert(vec![]).push(bus);
			}
		}
		let mut visited_buses = vec![false; routes.len()];
		let mut visited_stops = vec![false; 1000001];
		let mut queue = std::collections::VecDeque::new();
		queue.push_back(source);
		let mut level = 0;
		while !queue.is_empty() {
			level += 1;
			let mut size = queue.len();
			while size > 0 {
				size -= 1;
				let stop = queue.pop_front().unwrap();
				for &bus in stop_to_buses.get(&stop).unwrap_or(&vec![]) {
					if visited_buses[bus] {
						continue;
					}
					visited_buses[bus] = true;
					for &next_stop in routes[bus].iter() {
						if visited_stops[next_stop as usize] {
							continue;
						}
						visited_stops[next_stop as usize] = true;
						if next_stop == target {
							return level;
						}
						queue.push_back(next_stop);
					}
				}
			}
		}
		-1
    }
}

#[cfg(feature = "solution_815")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let routes: Vec<Vec<i32>> = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	let source: i32 = serde_json::from_str(&input_values[1]).expect("Failed to parse input");
	let target: i32 = serde_json::from_str(&input_values[2]).expect("Failed to parse input");
	json!(Solution::num_buses_to_destination(routes, source, target))
}
