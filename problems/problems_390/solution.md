# [Python/Java/JavaScript/Go] Recursion

> slug: pythonjavajavascriptgo-di-gui-by-himymbe-oro6
> date: 2022-01-02
> tags: Go, Java, JavaScript, Python, Python3
> question: Elimination Game (elimination-game)
> url: https://leetcode.cn/problems/elimination-game/solutions/eStndz/pythonjavajavascriptgo-di-gui-by-himymbe-oro6/

---
### Approach
```python3
# f(n) is the remaining number when elimination starts left to right; f'(n) starts right to left
# Symmetry: f(n) + f'(n) = n + 1
# Recurrence: f(n) = 2 * f'(n/2)
# Base case: f(1) = f'(1) = 1

# These conditions imply f(2 * n)/2 + f(n) = n + 1
# f(n)/2 + f(n/2) = n/2 + 1
# f(n) = (n/2 + 1 - f(n/2)) * 2
```

1. Left-to-right and right-to-left elimination are symmetric. For the same input $n$, their surviving numbers are symmetric about $\frac{n+1}{2}$, so $f(n) + f'(n) = n + 1$.
2. After left-to-right elimination, all remaining numbers are even. Divide them all by two and multiply the returned value by two. Since the next elimination is right to left, $f(n) = 2 * f'(\frac{n}{2})$.

### Code

```python3 []
class Solution:
    @lru_cache(None)
    def lastRemaining(self, n: int) -> int:
        return 2 * (n//2 + 1 - self.lastRemaining(n//2)) if n > 1 else 1
```
```Java []
class Solution {
    public int lastRemaining(int n) {
        return n > 1 ? 2 * (n/2 + 1 - lastRemaining(n/2)) : 1;
    }
}
```
```JavaScript []
/**
 * @param {number} n
 * @return {number}
 */
var lastRemaining = function(n) {
    return n > 1 ? 2 * (Math.floor(n/2) + 1 - lastRemaining(Math.floor(n/2))) : 1
};
```
```Go []
func lastRemaining(n int) int {
    if n > 1{
        return 2 * (n/2 + 1 - lastRemaining(n/2))
    }
    return 1
}
```
