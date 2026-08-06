# [Python/Java] 记忆化递归 or 动态规划

> slug: python-di-gui-shou-ji-xian-da-ge-qia-by-347jp
> date: 2021-09-03
> tags: Java, Python, Python3
> question: 斐波那契数 (fei-bo-na-qi-shu-lie-lcof)
> url: https://leetcode.cn/problems/fei-bo-na-qi-shu-lie-lcof/solutions/N4EgTi/python-di-gui-shou-ji-xian-da-ge-qia-by-347jp/

---
```python3
class Solution:
    mod = 10**9+7
    @lru_cache(None)
    def fib(self, n: int) -> int:
        return n if n <= 1 else (self.fib(n-1) + self.fib(n-2))% self.mod
```

```Python3 []
class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        a, b, mod = 0, 1, 10 ** 9 + 7
        for i in range(2, n + 1):
            a, b = b, (a + b) % mod
        return b
```
```Java []
class Solution {
    public int fib(int n) {
        if(n <= 1)
            return n;
        int b = 1, mod = (int)(1e9+7);
        for(int i=2, a=0, tmp=0; i<=n; i++){
            tmp = b;
            b = (a + b) % mod;
            a = tmp;
        }
        return b;
    }
}
```