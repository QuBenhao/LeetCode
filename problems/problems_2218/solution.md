# [Python] 前缀和 + 记忆化递归

> Author: Benhao
> Date: 2022-03-27
> Upvotes: 11
> Tags: Python, Python3

---

### 解题思路
换句话说就是暴力解法，对每个栈都讨论了当前能取到的最大值

dfs(idx, r)表示从piles[idx]开始，还可以取r次的最大值。
那么讨论从piles[idx]里取$x$个，其结果为后面还能取的最大值以及当前取走的和，也即 dfs(idx + 1, r - x) + sum(piles[idx][:x]) 【这里进行前缀和优化避免重复计算】,
找到其中的最大值即可

### 代码

```python3
class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        presums, n = [[0] + list(accumulate(p)) for p in piles], len(piles)
        
        @lru_cache(None)
        def dfs(idx, r):
            return max(dfs(idx + 1, r - i) + presums[idx][i] for i in range(min(r, len(piles[idx])) + 1)) if idx < n and r else 0
        
        return dfs(0, k)
```