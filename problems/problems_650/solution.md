# [Python/Java] 记忆化搜索 or (进阶)因数分解递归

> slug: pythonjava-ji-yi-hua-sou-suo-by-himymben-tx2s
> date: 2021-09-18
> tags: Java, Python, Python3
> question: 2 Keys Keyboard (2-keys-keyboard)
> url: https://leetcode.cn/problems/2-keys-keyboard/solutions/PJhAcJ/pythonjava-ji-yi-hua-sou-suo-by-himymben-tx2s/

---
### 解题思路
我们每次可以进行的操作是复制全部或者粘贴上去。当我们已经复制了目前的全部，就没有必要再复制了（这个时候只能粘贴）。
加上一个剪枝：如果当前剩余数除站帖数有余数，我们必然不能再构成答案。

注意到我们复制粘贴，永远是以某个因子进行的。就是说不管怎么粘贴，最开始的因子始终会被整除。换句话说：`我们只有在n的质因数的时候才能复制`，否则我们在其他时候复制将凑不出答案。
我们复制了一个数的最大的因数(除去自己)，需要复制粘贴目标数除上这个因数的次数。于是递归即可。

> 要出门儿了……关于往最大的因数递归是最优解回头再证明一下。

### 代码

```python3
class Solution:
    def minSteps(self, n: int) -> int:
        @lru_cache(None)
        def dfs(cur, paste):
            if cur == n:
                return 0
            elif cur > n:
                return inf
            if paste and (n - cur) % paste:
                return inf
            return min(dfs(cur, cur), dfs(cur + paste, paste)) + 1 if paste and paste != cur else (dfs(cur + paste, paste) + 1 if paste else dfs(cur, cur) + 1)
        return dfs(1, 0)
```

```Java []
class Solution {
    public int minSteps(int n) {
        if(n == 1)
            return 0;
        if(maxDivide(n) == n)
            return n;
        int d = maxDivide(n);
        return n/d + minSteps(d);
    }

    public int maxDivide(int n){
        for(int i=n/2;i>=2;i--)
            if(n%i == 0)
                return i;
        return n;
    }
}
```
```Python3 []
class Solution:
    def minSteps(self, n: int) -> int:
        return self.minSteps(d) + n//d if (n > 1 and (d:=self.maxDivide(n)) != n) else (n if n > 1 else 0)

    @lru_cache(None)
    def maxDivide(self, n):
        for i in range(n//2, 2, -1):
            if not n % i:
                return i
        return n
```