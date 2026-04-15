# [Python] 记忆化搜索(优化后~400ms)

> Author: Benhao
> Date: 2021-05-24
> Upvotes: 10
> Tags: Python, Python3

---

### 解题思路
每个长度为k的区间异或都为0，那么必然是`a_0 = a_k = ...`, `a_1 = a_k+1 = ...`, ...
且 `a_0 ^ a_1 ^ ... ^ a_k-1 = 0`

既然每组数都要变成同样的数，那么最小的代价是变为他们的众数。
只是全部变成众数不代表全部的异或结果能为0，需要枚举每组数中是否还需要变化。
`msv[idx]`为牺牲这组数的额外代价，也就是这组数全部变为不是这组数中的一个数，而这个数是其他组数的异或结果（故而保证为0）。
`dfs(idx+1,curr^key)`是说这组数选择了key作为他们的数后面需要的最小变化，那么需要的额外代价就是在刚刚的基础上放弃原来的众数变化`msv[idx] - counters[idx][key]`。

**优化** （~400ms）
加入剪枝，排序从需要最少的变化里开始统计（尽量选众数），估算至少要的变化代价`msv[idx] - counters[idx][key]`后，如果已经超过当前的`res`，不需要再进行dfs搜索.

### 代码

```python3
class Solution:
    def minChanges(self, nums: List[int], k: int) -> int:
        n = len(nums)
        counters = defaultdict(Counter)
        for i in range(k):
            for j in range(i, n, k):
                counters[i][nums[j]] += 1

        # 每组数的众数
        msv = [counters[i].most_common(1)[0][1] for i in range(k)]
        # 每组全部变为同样的数的最小代价
        ans = n - sum(msv)

        # 每组数都是众数，要满足异或为0，需要统计每组数选哪个数达到最优解，或者牺牲哪组数
        @lru_cache(None)
        def dfs(idx, curr):
            if idx == k and curr == 0:
                return 0
            elif idx == k:
                return float("inf")
            # 牺牲这组数的额外代价,所有数都换为某个数，使得异或为0
            res = msv[idx]
            # 变为这组数中的某个数
            for key in counters[idx].keys():
                res = min(res, dfs(idx+1, curr ^ key) - counters[idx][key] + msv[idx])
            return res
        return ans + dfs(0, 0) 

```
优化
```python3
class Solution:
    def minChanges(self, nums: List[int], k: int) -> int:
        n = len(nums)
        counters = defaultdict(Counter)
        for i in range(k):
            for j in range(i, n, k):
                counters[i][nums[j]] += 1
        
        # 每组数的众数
        msv = [counters[i].most_common(1)[0][1] for i in range(k)]
        # 每组全部变为同样的数的最小代价
        ans = n - sum(msv)

        # 每组数按频次排序的数
        keys = [sorted(counters[i].keys(),key=lambda x:-counters[i][x]) for i in range(k)]

        # 每组数都是众数，要满足异或为0，需要统计每组数选哪个数达到最优解，或者牺牲哪组数
        @lru_cache(None)
        def dfs(idx, curr):
            if idx == k and curr == 0:
                return 0
            elif idx == k:
                return float("inf")
            # 牺牲这组数的额外代价,所有数都换为某个数，使得异或为0
            res = msv[idx]
            # 变为这组数中的某个数
            for key in keys[idx]:
                if msv[idx] - counters[idx][key] >= res:
                    continue
                res = min(res, dfs(idx+1, curr ^ key) - counters[idx][key] + msv[idx])
            return res
        return ans + dfs(0, 0)
```