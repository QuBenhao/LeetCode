# [Python/Go] 动态规划(多路归并)

> Author: Benhao
> Date: 2022-02-17
> Upvotes: 2
> Tags: Go, Python, Python3

---

### 解题思路
新的丑数由之前的丑数乘以2、3、5之中的一个得到（保证质因子永远只有2、3、5），
我们可以维护三个坐标，记录每个质因子现在该乘的是第几个丑数。

### 代码

```Python3 []
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        dp = [0] * n
        dp[0] = 1
        idx2 = idx3 = idx5 = 0
        for i in range(1, n):
            a, b, c = dp[idx2] * 2, dp[idx3] * 3, dp[idx5] * 5
            m = min(a, b, c)
            if m == a:
                idx2 += 1
            if m == b:
                idx3 += 1
            if m == c:
                idx5 += 1
            dp[i] = m
        return dp[-1]
```
```Go []
func nthUglyNumber(n int) int {
    dp := make([]int, n)
    dp[0] = 1
    for i, idx2, idx3, idx5 := 1, 0, 0, 0; i < n; i++ {
        a, b, c := dp[idx2] * 2, dp[idx3] * 3, dp[idx5] * 5
        m := min(a, b, c)
        if m == a {
            idx2++
        }
        if m == b {
            idx3++
        }
        if m == c {
            idx5++
        }
        dp[i] = m
    }
    return dp[n - 1]
}

func min(vals ...int) int {
    ans := vals[0]
    for _, v := range vals {
        if v < ans {
            ans = v
        }
    }
    return ans
}
```