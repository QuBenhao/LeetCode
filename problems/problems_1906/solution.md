# [Python] Difference array (100%)

> Author: Benhao
> Date: 2021-06-20
> Upvotes: 2
> Tags: Python, Python3

---

### Approach
Use standard prefix differences. To determine which values occur in a range, keep prefix counts for every value from 1 through 100.

### Code

```python3
class Solution:
    def minDifference(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        # Difference array
        diff = [[0] * 101]
        for num in nums:
            diff.append(list(diff[-1]))
            diff[-1][num] += 1

        ans = []
        for l,r in queries:
            res = 100 # The maximum cannot exceed 100
            last = -100
            # Use prefix differences to find which values occur from l through r
            for i in range(1, 101):
                if diff[r + 1][i] - diff[l][i] > 0:
                    res = min(res, i - last)
                    last = i
            ans.append(res if res < 100 else -1)
        return ans
```
Some inputs never reach 100, so use the maximum value in nums instead.
```python3
class Solution:
    def minDifference(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        m = max(nums)
        # Difference array
        diff = [[0] * (m+1)]
        for num in nums:
            diff.append(list(diff[-1]))
            diff[-1][num] += 1

        ans = []
        for l,r in queries:
            res = m # The answer cannot exceed the maximum value
            last = -m # Ensure the first difference does not affect the result
            # Use prefix differences to find which values occur from l through r
            for i in range(1, m+1):
                if diff[r + 1][i] - diff[l][i] > 0:
                    res = min(res, i - last)
                    last = i
            ans.append(res if res < m else -1)
        return ans
```
