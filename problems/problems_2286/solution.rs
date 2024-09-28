use serde_json::{json, Value};


struct BookMyShow {
    n: usize,
    m: i32,
    min: Vec<i32>,
    sum: Vec<i64>,
}

impl BookMyShow {
    // 把下标 i 上的元素值增加 val
    fn update(&mut self, o: usize, l: usize, r: usize, i: usize, val: i32) {
        if l == r {
            self.min[o] += val;
            self.sum[o] += val as i64;
            return;
        }
        let m = (l + r) / 2;
        if i <= m {
            self.update(o * 2, l, m, i, val);
        } else {
            self.update(o * 2 + 1, m + 1, r, i, val);
        }
        self.min[o] = self.min[o * 2].min(self.min[o * 2 + 1]);
        self.sum[o] = self.sum[o * 2] + self.sum[o * 2 + 1];
    }

    // 返回区间 [L,R] 内的元素和
    fn query_sum(&self, o: usize, l: usize, r: usize, left: usize, right: usize) -> i64 {
        if left <= l && r <= right {
            return self.sum[o];
        }
        let mut res = 0;
        let m = (l + r) / 2;
        if left <= m {
            res = self.query_sum(o * 2, l, m, left, right);
        }
        if right > m {
            res += self.query_sum(o * 2 + 1, m + 1, r, left, right);
        }
        res
    }

    // 返回区间 [0,R] 中 <= val 的最靠左的位置，不存在时返回 -1
    fn find_first(&self, o: usize, l: usize, r: usize, right: usize, val: i32) -> i32 {
        if self.min[o] > val {
            return -1; // 整个区间的元素值都大于 val
        }
        if l == r {
            return l as i32;
        }
        let m = (l + r) / 2;
        if self.min[o * 2] <= val {
            return self.find_first(o * 2, l, m, right, val);
        }
        if right > m {
            return self.find_first(o * 2 + 1, m + 1, r, right, val);
        }
        -1
    }

    fn new(n: i32, m: i32) -> Self {
        let size = 2 << (32 - n.leading_zeros()) as usize;
        BookMyShow {
            n: n as usize,
            m,
            min: vec![0; size],
            sum: vec![0; size],
        }
    }

    fn gather(&mut self, k: i32, max_row: i32) -> Vec<i32> {
        // 找第一个能倒入 k 升水的水桶
        let r = self.find_first(1, 0, self.n - 1, max_row as usize, self.m - k);
        if r < 0 {
            return vec![]; // 没有这样的水桶
        }
        let c = self.query_sum(1, 0, self.n - 1, r as usize, r as usize) as i32;
        self.update(1, 0, self.n - 1, r as usize, k); // 倒水
        vec![r, c]
    }

    fn scatter(&mut self, mut k: i32, max_row: i32) -> bool {
        // [0,maxRow] 的接水量之和
        let s = self.query_sum(1, 0, self.n - 1, 0, max_row as usize);
        if s > (self.m as i64 * (max_row + 1) as i64) - k as i64 {
            return false; // 水桶已经装了太多的水
        }
        // 从第一个没有装满的水桶开始
        let mut i = self.find_first(1, 0, self.n - 1, max_row as usize, self.m - 1) as usize;
        while k > 0 {
            let left = k.min(self.m - self.query_sum(1, 0, self.n - 1, i, i) as i32);
            self.update(1, 0, self.n - 1, i, left); // 倒水
            k -= left;
            i += 1;
        }
        true
    }
}

/**
 * Your BookMyShow object will be instantiated and called as such:
 * let obj = BookMyShow::new(n, m);
 * let ret_1: Vec<i32> = obj.gather(k, maxRow);
 * let ret_2: bool = obj.scatter(k, maxRow);
 */

#[cfg(feature = "solution_2286")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let operators: Vec<String> = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	let op_values: Vec<Vec<Value>> = serde_json::from_str(&input_values[1]).expect("Failed to parse input");
	let n_obj: i32 = serde_json::from_value(op_values[0][0].clone()).expect("Failed to parse input");
	let m_obj: i32 = serde_json::from_value(op_values[0][1].clone()).expect("Failed to parse input");
	let mut obj = BookMyShow::new(n_obj, m_obj);
	let mut ans: Vec<Option<Value>> = vec![];
	for i in 1..operators.len() {
		match operators[i].as_str() {
			"gather" => {
				let k: i32 = serde_json::from_value(op_values[i][0].clone()).expect("Failed to parse input");
				let max_row: i32 = serde_json::from_value(op_values[i][1].clone()).expect("Failed to parse input");
				ans.push(Some(Value::from(obj.gather(k, max_row))));
			},
			"scatter" => {
				let k: i32 = serde_json::from_value(op_values[i][0].clone()).expect("Failed to parse input");
				let max_row: i32 = serde_json::from_value(op_values[i][1].clone()).expect("Failed to parse input");
				ans.push(Some(Value::from(obj.scatter(k, max_row))));
			},
			_ => ans.push(None),
		}
	}
	json!(ans)
}
