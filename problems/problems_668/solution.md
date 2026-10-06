# [Python/Java/JavaScript/Go] Binary search

> slug: pythonjavajavascriptgo-er-fen-by-himymbe-wz4r
> date: 2022-05-17
> tags: Go, Java, JavaScript, Python, Python3
> question: Kth Smallest Number in Multiplication Table (kth-smallest-number-in-multiplication-table)
> url: https://leetcode.cn/problems/kth-smallest-number-in-multiplication-table/solutions/n3MplD/pythonjavajavascriptgo-er-fen-by-himymbe-wz4r/

---
### Approach
The kth smallest value in a multiplication table is not obvious, but counting values below a given $x$ is easy: row $i$ contributes $\frac{x}{i}$.
Binary search the table's value range using the count of smaller values to locate the position corresponding to k.

You might ask: does this range also contain prime numbers absent from the multiplication table?
The monotonic count is the same at such a prime and at the nearest smaller table value. We choose the left boundary, which is the table value. This is also why the Python code uses bisect_left rather than bisect_right.

PS:
A small optimization: swap the dimensions so the counting step uses the smaller number of rows.

### Code

```Python3 []
class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        return bisect_left(range(m * n + 1), k, key=lambda x:sum(min(n, x // i) for i in range(1, m + 1))) if n >= m else self.findKthNumber(n, m, k)
```
```Java []
class Solution {
    public int findKthNumber(int m, int n, int k) {
        if (m > n) {
            int tmp = m;
            m = n;
            n = tmp;
        }
        int left = 0, right = m * n;
        while(left < right) {
            int mid = left + right >> 1;
            if (count(m, n, mid) >= k) {
                right = mid;
            } else {
                left = mid + 1;
            }
        }
        return left;
    }

    private int count(int m, int n, int x) {
        int sum = 0;
        for(int i = 1; i <= m; i++) {
            sum += Math.min(n, x / i);
        }
        return sum;
    }
}
```
```JavaScript []
/**
 * @param {number} m
 * @param {number} n
 * @param {number} k
 * @return {number}
 */
var findKthNumber = function(m, n, k) {
    if (m > n) {
        [m, n] = [n, m]
    }
    let left = 0, right = m * n
    const check = (x) => {
        let sum = 0
        for(let i = 1; i<= m; i++) {
            sum += Math.min(n, Math.floor(x / i))
        }
        return sum
    }
    while(left < right) {
        const mid = (left + right) >> 1
        if (check(mid) >= k) {
            right = mid
        } else {
            left = mid + 1
        }
    }
    return left
};
```
```Go []
func findKthNumber(m int, n int, k int) int {
    if m > n {
        m, n = n, m
    }
    left, right := 0, m * n
    check := func(x int) (sum int) {
        for i := 1; i <= m; i++ {
            if cur := x / i; cur <= n {
                sum += cur
            } else {
                sum += n
            }
        }
        return
    }
    for left < right {
        mid := (left + right) >> 1
        if check(mid) >= k {
            right = mid
        } else {
            left = mid + 1
        }
    }
    return left
}
```
