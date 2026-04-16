# [Python] 二分法，给定一个值是否存在这个构造

> Author: Benhao
> Date: 2021-03-21
> Upvotes: 2
> Tags: Python

---

### 解题思路
当我们知道index位置的最大值时，我们很容易求得两侧分别的和的最小值，如果这个值比最大和还要大，显然这个最大值不合理。

### 代码

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