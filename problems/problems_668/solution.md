# [Python/Java/JavaScript/Go] 二分

> slug: pythonjavajavascriptgo-er-fen-by-himymbe-wz4r
> date: 2022-05-17
> tags: Go, Java, JavaScript, Python, Python3
> question: Kth Smallest Number in Multiplication Table (kth-smallest-number-in-multiplication-table)
> url: https://leetcode.cn/problems/kth-smallest-number-in-multiplication-table/solutions/n3MplD/pythonjavajavascriptgo-er-fen-by-himymbe-wz4r/

---
### 解题思路
乘法表中第k小的数并不能直观地得到, 但是乘法表中的某个数$x$，比它小的数有多少个是很好统计的(每行$i$都是$\frac{x}{i}$个)。
对乘法表的值域做比它小的个数的二分，找到k对应的位置。

有朋友可能问了，这个值域中还包括并不在乘法表中的质数呢？
根据二段性，比这个质数小一点的乘法表中的数和这个质数，在这个乘法表中小于它的个数是一样的，我们会取左边界也就是乘法表里的数(这也是为啥Py里用bisect_left而不是bisect_right)。

PS:
小优化，交换行数，对小的行数统计二分值

### 代码

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