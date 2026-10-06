# [Python] Binary search: can a given value be constructed?

> Author: Benhao
> Date: 2021-03-21
> Upvotes: 2
> Tags: Python

---

### Approach
For a candidate maximum at index, compute the minimum sums on both sides. If the total exceeds the allowed maximum sum, the candidate is infeasible.

### Code

```python
class Solution(object):
    def maxValue(self, n, index, maxSum):
        """
        :type n: int
        :type index: int
        :type maxSum: int
        :rtype: int
        """
        def helper(val):
            if val > index:
                l = (val-1 + val-index) * index // 2
            else:
                l = (val-1 + 1) * (val -1) // 2 + (index - val + 1)
            if val > n - 1 - index:
                r = (val-1+val - n + 1 + index) * (n -1 - index) // 2
            else:
                r = (val-1+1) *(val-1) //2 + (n-1-index - val +1)
            return l + r > maxSum - val
            
        left, right = 1, maxSum - n + 1
        while left < right:
            mid = (left+right)//2
            if helper(mid):
                right = mid
            else:
                left = mid + 1
        return left if not helper(left) else left - 1
```
