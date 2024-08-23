use serde_json::{json, Value};

pub struct Solution;

impl Solution {
    pub fn find_products_of_elements(queries: Vec<Vec<i64>>) -> Vec<i32> {
        let mut ans = Vec::new();
        for query in queries.iter() {
            // 偏移让数组下标从1开始
            let mut query = query.clone();
            query[0] += 1;
            query[1] += 1;
            let l = Self::mid_check(query[0]);
            let r = Self::mid_check(query[1]);
            let mod_val = query[2];
            let mut res = 1i64;
            let mut pre = Self::count_one(l - 1);
            for j in 0..60 {
                if (1i64 << j) & l != 0 {
                    pre += 1;
                    if pre >= query[0] && pre <= query[1] {
                        res = res * (1i64 << j) % mod_val;
                    }
                }
            }
            if r > l {
                let mut bac = Self::count_one(r - 1);
                for j in 0..60 {
                    if (1i64 << j) & r != 0 {
                        bac += 1;
                        if bac >= query[0] && bac <= query[1] {
                            res = res * (1i64 << j) % mod_val;
                        }
                    }
                }
            }

            if r - l > 1 {
                let xs = Self::count_pow(r - 1) - Self::count_pow(l);
                res = res * Self::pow_mod(2, xs, mod_val) % mod_val;
            }
            ans.push(res as i32);
        }

        ans
    }

    // 计算 <= x 所有数的数位1的和
    fn count_one(x: i64) -> i64 {
        let mut res = 0i64;
        let mut sum = 0i64;

        for i in (0..=60).rev() {
            if (1i64 << i) & x != 0 {
                res += sum * (1i64 << i);
                sum += 1;
                if i > 0 {
                    res += i * (1i64 << (i - 1));
                }
            }
        }
        res += sum;
        res
    }

    // 计算 <= x 所有数的数位对幂的贡献之和
    fn count_pow(x: i64) -> i64 {
        let mut res = 0i64;
        let mut sum = 0i64;
        for i in (0..=60).rev() {
            if (1i64 << i) & x != 0 {
                res += sum * (1i64 << i);
                sum += i;
                if i > 0 {
                    res += i * (i - 1) / 2 * (1i64 << (i - 1));
                }
            }
        }
        res += sum;
        res
    }

    fn pow_mod(mut x: i64, mut y: i64, mod_val: i64) -> i64 {
        let mut res = 1i64;
        while y != 0 {
            if y & 1 != 0 {
                res = res * x % mod_val;
            }
            x = x * x % mod_val;
            y >>= 1;
        }
        res
    }

    fn mid_check(x: i64) -> i64 {
        let mut l = 1i64;
        let mut r = 1_000_000_000_000_000i64;
        while l < r {
            let mid = (l + r) >> 1;
            if Self::count_one(mid) >= x {
                r = mid;
            } else {
                l = mid + 1;
            }
        }
        r
    }
}


#[cfg(feature = "solution_3145")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let queries: Vec<Vec<i64>> = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	json!(Solution::find_products_of_elements(queries))
}
