# [Python] 数学

> slug: python-shu-xue-by-himymben-4ypu
> date: 2022-05-01
> tags: Python, Python3
> question: Elements in Array After Removing and Replacing Elements (elements-in-array-after-removing-and-replacing-elements)
> url: https://leetcode.cn/problems/elements-in-array-after-removing-and-replacing-elements/solutions/GYEghw/python-shu-xue-by-himymben-4ypu/

---
### 解题思路
根本不需要模拟，2n一循环，每个时刻的坐标都很好推。

### 代码

```python3
class Solution:
    def elementInNums(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        n = len(nums)
        ans = [-1] * len(queries)
        for i, (t, idx) in enumerate(queries):
            t %= 2 * n
            if t < n and idx < n - t:
                ans[i] = nums[t + idx]
            elif t > n and idx < t - n:
                ans[i] = nums[idx]
        return ans
```