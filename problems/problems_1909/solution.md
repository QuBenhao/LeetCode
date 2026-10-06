# [Python] Delete and check

> Author: Benhao
> Date: 2021-06-27
> Upvotes: 6
> Tags: Python, Python3

---

### Approach
I felt an easy problem should not need a complicated solution, so I wrote this.
At the first non-increasing adjacent pair, try deleting each element separately. Return True if either resulting array is strictly increasing.
Otherwise, return False.

### Code

```python3
class Solution:
    def canBeIncreasing(self, nums: List[int]) -> bool:
        idx = None
        for i in range(len(nums)-1):
            if nums[i+1] <= nums[i]:
                idx = i
                break
        if idx is None:
            return True
        nums1 = nums[:idx] + nums[idx+1:]
        nums2 = nums[:idx+1] + nums[idx+2:]
        ans1 = ans2 = True
        for i in range(len(nums1)-1):
            if nums1[i+1] <= nums1[i]:
                ans1 = False
            if nums2[i+1] <= nums2[i]:
                ans2 = False
        return ans1 or ans2
```
