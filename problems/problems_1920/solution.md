# [Python] 直接写就行

> Author: Benhao
> Date: 2021-07-04
> Upvotes: 1
> Tags: Python, Python3

---

### 解题思路
模拟

### 代码

```python3
class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        return [nums[nums[i]] for i in range(len(nums))]
```