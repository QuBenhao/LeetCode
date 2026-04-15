# [Python/Go] 动态规划

> Author: Benhao
> Date: 2022-02-16
> Upvotes: 1
> Tags: Go, Python, Python3

---

### 解题思路
当前坐标的方案数有以下关系：
如果当前字符不是0，那么它本身可以构成一种方案，所以可以叠加上一个坐标的方案数；
如果当前字符和上个字符组成的数字介于10到26之间，那么它们可以组合起来构成一种方案，所以可以叠加上上个坐标的方案数。

### 代码

```Python3 []
class Solution:
    def numDecodings(self, s: str) -> int:
        dp0, dp1 = 1, int(s[0] != '0')
        for i in range(1, len(s)):
            dp = 0
            if s[i] != '0':
                dp += dp1
            if 10 <= int(s[i-1:i+1]) <= 26:
                dp += dp0
            dp0, dp1 = dp1, dp
        return dp1
```
```Go []
func numDecodings(s string) int {
    dp0, dp1 := 1, 1
    if s[0] == '0' {
        dp1 = 0
    }
    for i := 1; i < len(s); i++ {
        dp := 0
        if s[i] != '0' {
            dp += dp1
        }
        if v := (s[i-1] - '0') * 10 + (s[i] - '0'); 10 <= v && v <= 26 {
            dp += dp0
        }
        dp0, dp1 = dp1, dp
    }
    return dp1
}
```