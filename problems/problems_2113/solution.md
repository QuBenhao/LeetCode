# [Python] Mathematics

> slug: python-shu-xue-by-himymben-4ypu
> date: 2022-05-01
> tags: Python, Python3
> question: Elements in Array After Removing and Replacing Elements (elements-in-array-after-removing-and-replacing-elements)
> url: https://leetcode.cn/problems/elements-in-array-after-removing-and-replacing-elements/solutions/GYEghw/python-shu-xue-by-himymben-4ypu/

---
### Approach
The process repeats every 2n steps, so each position is easy to derive directly.

### Code

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
