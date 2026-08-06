# [Python] 前缀和+二分查找

> slug: python-er-by-himymben-xxc7
> date: 2022-03-13
> tags: Python, Python3
> question: 剧情触发时间 (ju-qing-hong-fa-shi-jian)
> url: https://leetcode.cn/problems/ju-qing-hong-fa-shi-jian/solutions/vCyC04/python-er-by-himymben-xxc7/

---
### 解题思路
三个维度其实和一个维度的代码没有什么区别

### 代码

```python3
class Solution:
    def getTriggerTime(self, increase: List[List[int]], requirements: List[List[int]]) -> List[int]:
        presum1 = [0] + list(accumulate(list(zip(*increase))[0]))
        presum2 = [0] + list(accumulate(list(zip(*increase))[1]))
        presum3 = [0] + list(accumulate(list(zip(*increase))[2]))
        ans, n = [-1] * len(requirements), len(increase) + 1
        for i, v in enumerate(requirements):
            a, b, c = v
            idx1, idx2, idx3 = bisect_left(presum1, a), bisect_left(presum2, b), bisect_left(presum3, c)
            if idx1 < n and idx2 < n and idx3 < n:
                ans[i] = max(idx1, idx2, idx3)
        return ans
```