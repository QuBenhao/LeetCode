# [Python/Go] Dynamic programming -> mathematics

> slug: pythongo-dong-tai-gui-hua-shu-xue-by-him-6ddz
> date: 2022-02-27
> tags: Go, Python, Python3
> question: Integer Break (integer-break)
> url: https://leetcode.cn/problems/integer-break/solutions/oMkl5l/pythongo-dong-tai-gui-hua-shu-xue-by-him-6ddz/

---
### Approach
Use dynamic programming to store the maximum product for each integer, then enumerate splits to find the current maximum.

Mathematics:
This is also a Codeforces problem: split off as many 3s as possible to maximize the product. If the remainder modulo 3 is 1, use one fewer 3 and make a 4 as 2*2; if it is 2, append a 2.
Any number greater than 4 can be split into numbers with a larger product, and 4 itself is 2*2. Thus, only factors 1, 2, and 3 need consideration.
A factor of 1 contributes the least. Comparing 2 and 3, 3+3=2+2+2 but 3*3>2*2*2, so splitting into 3s is optimal.

### Code

```Python3 []
class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [0] * (n + 1)
        for i in range(2, n + 1):
            dp[i] = i - 1
            for j in range(1, i // 2 + 1):
                dp[i] = max(dp[i], j * (i - j), j * dp[i - j])
        return dp[n]
```
```Go []
func integerBreak(n int) int {
    dp := make([]int, n + 1)
    for i := 2; i <= n; i++ {
        for j := 1; j < i / 2 + 1; j++ {
            dp[i] = max(dp[i], j * (i - j), j * dp[i - j])
        }
    }
    return dp[n]
}

func max(vals ...int) int {
    ans := vals[0]
    for _, v := range vals {
        if v > ans {
            ans = v
        }
    }
    return ans
}
```

Mathematics
```Python3 []
class Solution:
    def integerBreak(self, n: int) -> int:
        match n:
            case 2:
                return 1
            case 3:
                return 2
        match n % 3:
            case 0:
                return 3 ** (n // 3)
            case 1:
                return 3 ** ((n - 4) // 3) * 4
            case 2:
                return 3 ** ((n - 2) // 3) * 2
```
```Go []
func integerBreak(n int) int {
    if n == 2 {
        return 1
    } else if n == 3 {
        return 2
    }
    if r := n % 3; r == 0 {
        return pow(3, n / 3)
    } else if r == 1 {
        return pow(3, (n - 4) / 3) * 4
    } else {
        return pow(3, (n - 2) / 3) * 2
    }
}

func pow(a, b int) int {
    ans := 1
    for b > 0 {
        if b & 1 == 1 {
            ans *= a
        }
        a *= a
        b >>= 1
    }
    return ans
}
```
