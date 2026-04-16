# [Python] 贪心

> Author: Benhao
> Date: 2021-08-15
> Upvotes: 0
> Tags: Python, Python3

---

```python3
class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        nums.sort()
        mid = (len(nums) + 1) // 2
        nums[::2], nums[1::2] = nums[:mid], nums[mid:]
        return nums
```