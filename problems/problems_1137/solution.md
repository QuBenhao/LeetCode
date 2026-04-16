# [Python/Go] 递归/动态规划

> Author: Benhao
> Date: 2021-08-07
> Upvotes: 5
> Tags: Go, Python, Python3

---

```Python3 []
class Solution:
    @lru_cache(None)
    def tribonacci(self, n: int) -> int:
        return n if n <= 1 else (1 if n == 2 else self.tribonacci(n - 1) + self.tribonacci(n - 2) + self.tribonacci(n - 3))
```
```Go []
func tribonacci(n int) int {
    if n == 0 {
        return 0
    }
    a, b, c := 0, 1, 1
    for i := 2; i < n; i++ {
        a, b, c = b, c, a + b + c
    }
    return c
}
```