# [Python/Java/JavaScript/Go] 递归

> slug: pythonjavajavascriptgo-di-gui-by-himymbe-oro6
> date: 2022-01-02
> tags: Go, Java, JavaScript, Python, Python3
> question: Elimination Game (elimination-game)
> url: https://leetcode.cn/problems/elimination-game/solutions/eStndz/pythonjavajavascriptgo-di-gui-by-himymbe-oro6/

---
### 解题思路
```python3
# f(n) 表示从左到右剩下的数字的结果, f'(n) 表示从右到左删除的结果
# 对称性: f(n) + f'(n) = n + 1
# 递归性: f(n) = 2 * f'(n/2)
# 初始条件: f(1) = f'(1) = 1

# 根据以上条件可得: f(2 * n)/2 + f(n) = n + 1
# f(n)/2 + f(n/2) = n/2 + 1
# f(n) = (n/2 + 1 - f(n/2)) * 2
```

1. 从左到右删和从右到左删满足对称性，同样的输入$n$，从左到右删完剩下的数和从右到左删完剩下的数满足$\frac{n+1}{2}$中心对称，所以$f(n) + f'(n) = n + 1$
2. 从左到右删完以后，剩下的数都是偶数，可以统一除二最后返回的数再乘二处理，因为该从右往左删了，故$f(n) = 2 * f'(\frac{n}{2})$

### 代码

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