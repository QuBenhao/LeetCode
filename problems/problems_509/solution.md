# [Python/Go] Recursion/Dynamic programming

> slug: pythongo-di-gui-dong-tai-gui-hua-by-himy-m6fw
> date: 2022-02-07
> tags: Go, Python, Python3
> question: Fibonacci Number (fibonacci-number)
> url: https://leetcode.cn/problems/fibonacci-number/solutions/zq3Leg/pythongo-di-gui-dong-tai-gui-hua-by-himy-m6fw/

---
### Approach
f(n) = f(n - 1) + f(n - 2)

### Code

```Python3 []
class Solution:
    @lru_cache(None)
    def fib(self, n: int) -> int:
        return 0 if not n else (1 if n == 1 else self.fib(n - 1) + self.fib(n - 2))
```
```Go []
func fib(n int) int {
    if n == 0 {
        return 0
    }
    f0, f1 := 0, 1
    for i := 2 ; i <= n; i++ {
        f0, f1 = f1, f0 + f1
    }
    return f1
}
```
