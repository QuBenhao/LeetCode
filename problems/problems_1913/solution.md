# [Python] 贪心

> Author: Benhao
> Date: 2021-06-27
> Upvotes: 6
> Tags: Python, Python3

---

### 解题思路
两个最大的减去两个最小的

### 代码

```python3
class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        nums.sort()
        return nums[-1] * nums[-2] - nums[0] * nums[1]

```