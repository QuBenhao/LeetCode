# [Python] Greedy

> Author: Benhao
> Date: 2021-06-27
> Upvotes: 6
> Tags: Python, Python3

---

### Approach
Subtract the product of the two smallest values from the product of the two largest.

### Code

```python3
class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        nums.sort()
        return nums[-1] * nums[-2] - nums[0] * nums[1]

```
