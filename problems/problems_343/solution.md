# [Python/Go] 动态规划 -> 数学

> slug: pythongo-dong-tai-gui-hua-shu-xue-by-him-6ddz
> date: 2022-02-27
> tags: Go, Python, Python3
> question: Integer Break (integer-break)
> url: https://leetcode.cn/problems/integer-break/solutions/oMkl5l/pythongo-dong-tai-gui-hua-shu-xue-by-him-6ddz/

---
### 解题思路
动态规划维护每个数字最大的拆分乘机，然后遍历枚举拆分数求当前最大即可。

数学：
实际上也是CF上的一道题，尽可能地拆3乘积最大。如果模3余1要少拆一个3，凑出一个4作为2*2；如果模3余2就最后拼一个2即可。
这是因为，超过4的数字拆成多个数字乘积都会比原数字大，4本身又是2*2，那么考虑的因数本身就只有1、2、3。
1肯定是最没有贡献的。2和3的对比来说，3+3=2+2+2，但是3*3>2*2*2，所以拆3是最优的。

### 代码

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

数学
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