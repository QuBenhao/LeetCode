use serde_json::{json, Value};

pub struct Solution;

impl Solution {
    pub fn latest_time_catch_the_bus(buses: Vec<i32>, passengers: Vec<i32>, capacity: i32) -> i32 {
        let mut buses = buses;
        let mut passengers = passengers;
        buses.sort_unstable();
        passengers.sort_unstable();
        let mut j: i32 = 0;
        let n: i32 = passengers.len() as i32;
        let mut c: i32 = 0;
        for &bus in buses.iter() {
            c = capacity;
            while c > 0 && j < n && passengers[j as usize] <= bus {
                c -= 1;
                j += 1;
            }
        }
        j -= 1;
        let mut ans: i32;
        if c > 0 {
            ans = buses[buses.len() - 1];
        } else {
            ans = passengers[j as usize];
        }
        while j >= 0 && passengers[j as usize] == ans {
            j -= 1;
            ans -= 1;
        }
        ans
    }
}

#[cfg(feature = "solution_2332")]
pub fn solve(input_string: String) -> Value {
    let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
    let buses: Vec<i32> = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
    let passengers: Vec<i32> = serde_json::from_str(&input_values[1]).expect("Failed to parse input");
    let capacity: i32 = serde_json::from_str(&input_values[2]).expect("Failed to parse input");
    json!(Solution::latest_time_catch_the_bus(buses, passengers, capacity))
}
