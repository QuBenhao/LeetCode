# [Python/Go] Dynamic programming (multiway merge)

> Author: Benhao
> Date: 2022-02-17
> Upvotes: 2
> Tags: Go, Python, Python3

---

### Approach
Each new ugly number is an earlier ugly number multiplied by 2, 3, or 5, ensuring that its only prime factors remain 2, 3, and 5.
Maintain three indices to record which ugly number each prime factor should multiply next.

### Code

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
