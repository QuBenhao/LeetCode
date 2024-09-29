use serde_json::{json, Value};

pub struct Solution;

impl Solution {
    pub fn time_required_to_buy(tickets: Vec<i32>, k: i32) -> i32 {
        let k = k as usize;
        let ticket_to_buy = tickets[k];
        let mut ans: i32 = 0;
        let mut iter = tickets.iter().enumerate();
        while let Some((i, &ticket)) = iter.next() {
            if i > k {
                ans += ticket.min(ticket_to_buy - 1);
            } else {
                ans += ticket.min(ticket_to_buy);
            }
        }
        ans
    }
}

#[cfg(feature = "solution_2073")]
pub fn solve(input_string: String) -> Value {
    let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
    let tickets: Vec<i32> = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
    let k: i32 = serde_json::from_str(&input_values[1]).expect("Failed to parse input");
    json!(Solution::time_required_to_buy(tickets, k))
}
