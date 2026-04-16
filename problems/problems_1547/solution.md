# [Python] 记忆化递归

> Author: Benhao
> Date: 2022-03-26
> Upvotes: 2
> Tags: Python, Python3

---

### 解题思路
TODO：优化

### 代码

```python3
class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        cuts.sort()

        @lru_cache(None)
        def dfs(l, r, idx_l, idx_r):
            if r <= l or idx_r <= idx_l:
                return 0
            return min(dfs(l, cuts[idx], idx_l, idx) + dfs(cuts[idx], r, idx + 1, idx_r) for idx in range(idx_l, idx_r)) + r - l
        
        return dfs(0, n, 0, len(cuts))
```