# [Python] 差分数组(100%)

> Author: Benhao
> Date: 2021-06-20
> Upvotes: 2
> Tags: Python, Python3

---

### 解题思路
很标准的差分。我们需要知道不同区间之间有哪些数，所以前缀统计每个区间不同的数的个数(1-100)。

### 代码

```python3
class Solution:
    def minDifference(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        # 差分数组
        diff = [[0] * 101]
        for num in nums:
            diff.append(list(diff[-1]))
            diff[-1][num] += 1

        ans = []
        for l,r in queries:
            res = 100 # 最大不会超过100
            last = -100
            # 我们通过差分数组求得l到r之间有哪些数
            for i in range(1, 101):
                if diff[r + 1][i] - diff[l][i] > 0:
                    res = min(res, i - last)
                    last = i
            ans.append(res if res < 100 else -1)
        return ans
```
有的数据可能用不到100那么大，用nums里的最大值即可
```python3
class Solution:
    def minDifference(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        m = max(nums)
        # 差分数组
        diff = [[0] * (m+1)]
        for num in nums:
            diff.append(list(diff[-1]))
            diff[-1][num] += 1

        ans = []
        for l,r in queries:
            res = m # 最大不会超过最大值
            last = -m # 保证第一个数做差不影响结果
            # 我们通过差分数组求得l到r之间有哪些数
            for i in range(1, m+1):
                if diff[r + 1][i] - diff[l][i] > 0:
                    res = min(res, i - last)
                    last = i
            ans.append(res if res < m else -1)
        return ans
```