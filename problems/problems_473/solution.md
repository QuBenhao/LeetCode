# [Python] 状态压缩+记忆化递归

> slug: python-zhuang-tai-ya-suo-ji-yi-hua-di-gu-7jsc
> date: 2021-08-07
> tags: Python, Python3
> question: Matchsticks to Square (matchsticks-to-square)
> url: https://leetcode.cn/problems/matchsticks-to-square/solutions/mOXss7/python-zhuang-tai-ya-suo-ji-yi-hua-di-gu-7jsc/

---
### 解题思路
我们能用所有火柴构成正方形，首先必然有和为4的倍数，边为和除以4(且没有火柴大于这个边长)。
用状态压缩记录用过的火柴，和当前构建的边的和，如果达到边长，就清0构造下一个边长。
直到我们用光所有火柴

### 代码

```python3
class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        total = sum(matchsticks)
        if total % 4 != 0:
            return False
        line = total // 4
        if any(num > line for num in matchsticks):
            return False
        n = len(matchsticks)
        final = (1 << n) - 1
        
        @lru_cache(None)
        def dfs(state, cur):
            if cur == line:
                cur = 0
                if state == final:
                    return True
            for i in range(n):
                if not 1 << i & state and cur + matchsticks[i] <= line:
                    if dfs(1 << i | state, cur + matchsticks[i]):
                        return True
            return False
        
        return dfs(0, 0)
```