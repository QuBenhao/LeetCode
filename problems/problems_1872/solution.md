# [Python] 动态规划(倒序) or 记忆化搜索(正序)

> Author: Benhao
> Date: 2021-05-23
> Upvotes: 3
> Tags: Python, Python3

---

### 解题思路
1. 我们必须注意到的是，取的所有分数要放回去这个操作，本质是**不改变前缀和**的。
2. 我们从i能取到的最大收益，是依赖于i右边的j能取到的最大收益的（反向递推的原因）
这是因为:
```
dp[i] = max(presum[j] - dp[j] for j in range(i+1, n-1))
```
上面的式子在倒序递推的时候可以压缩为一维:
取`presum-res`可以理解为i取到最优的j，取`res`可以理解为不取到j，跨过j获得j位置能取到的最大值
```
res = max(res, presum - res)
```
此处的presum对应res的j

参考自[链接](https://leetcode.com/problems/stone-game-viii/discuss/1224639/Python-prefix-sum)

### 代码

```python3
class Solution:
    def stoneGameVIII(self, stones: List[int]) -> int:
        # 1. 每次取走最左边的x个石子，把他们的和放回最左边，前缀和presum[x]不变
        # 2. 位置i的最大收益为i右边最大的 presum[j] - dp[j] 的j
        for i in range(1, len(stones)):
            stones[i] += stones[i-1]

        res = stones[-1]
        for num in stones[-2:0:-1]:
            # 我们取到j，获得presum[j]的分数，对手最多能取dp[j]
            # 或者我们跨过j，获得dp[j]的分数
            res = max(num - res, res)
        return res

```
直接搜索使用记忆化记录一定范围的最大值勉强能过
```python3
class Solution:
    def stoneGameVIII(self, stones: List[int]) -> int:
        # 移除并放回，前缀和不变
        # 每次拿的石子必然包括前面的前缀和
        @lru_cache(None)
        def dfs(idx):
            if idx >= n - 1:
                return presum[n]
            # 不选当前坐标，选后面的会是dfs(idx+1),选当前坐标会得到presum[idx+1] - dfs(idx+1)。取两者最大值
            return max(dfs(idx + 1), presum[idx + 1] - dfs(idx+1))

        n = len(stones)
        presum = [0] + list(accumulate(stones))
        dfs.cache_clear()
        return dfs(1)
```