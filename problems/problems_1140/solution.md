# [Python] 记忆化搜索+前缀和加速

> Author: Benhao
> Date: 2021-06-16
> Upvotes: 2
> Tags: Python, Python3

---

### 解题思路
我们要统计先手最多拿多少石头，那么后手的目的就是让先手拿到的尽可能的小。
先手拿的时候要根据前缀和计算当前选择拿到的石子数叠加递归得到的石子数。

在最大最小博弈中，常见的有使用减来实现实际的交替。(Alice取的全为正，Bob取的全为负)

### 代码

```python3
class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        @lru_cache(None)
        def dfs(idx, curr, p):
            if idx == n:
                return 0
            # 剩余的全部石子可以被一个人拿走了
            if n - idx <= 2 * curr:
                return presum[-1] - presum[idx] if p else 0
            # Alice拿石子要找后面最大的结果
            if p:
                return max(dfs(idx + i, max(curr, i), not p) + presum[idx + i]
                           for i in range(1,2 * curr + 1)) - presum[idx]
            # Bob要选使得Alice拿的最小的选择
            return min(dfs(idx + i, max(curr, i), not p) for i in range(1, 2 * curr + 1))

        n = len(piles)
        presum = list(accumulate([0] + piles))
        return dfs(0, 1, True)
```
用负号代替p的交替
```python3
class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        @lru_cache(None)
        def dfs(idx, curr):
            if idx == n:
                return 0
            # 剩余的全部石子可以被一个人拿走了
            if n - idx <= 2 * curr:
                return presum[-1] - presum[idx]
            # 当前能拿到的最大值为 总共剩余的石子减去让对方拿到的尽可能小
            return presum[-1] - presum[idx] - min(dfs(idx + i, max(i, curr)) for i in range(1, 2 * curr + 1))

        n = len(piles)
        presum = list(accumulate([0] + piles))
        return dfs(0, 1)
```