# [Python/Go] Dynamic programming

> Author: Benhao
> Date: 2022-02-16
> Upvotes: 1
> Tags: Go, Python, Python3

---

### Approach
The number of ways at the current index follows these relationships:
If the current character is not 0, it can form a decoding on its own, so add the number of ways at the previous index;
if the previous and current characters form a number from 10 through 26, they can form a decoding together, so add the number of ways two indices back.

### Code

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
