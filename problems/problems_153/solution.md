# [Python] Find the rotation point with binary search

> Author: Benhao
> Date: 2021-04-08
> Upvotes: 1
> Tags: Python, Python3

---

### Approach
If left is smaller than right, left is the minimum from left to right;
If mid is smaller than right, the rotation point is at mid or to its left. For example, in [5,1,2,3,4], `right = 4` and `mid = 2`, so the minimum is to the left of mid.
If mid is greater than left, the rotation point is to the right of mid. For example, in [3,4,5,1,2], `left = 3` and `mid = 5`, so the minimum is to the right of mid.
**nums[right]<nums[mid]<nums[left] cannot occur**

### Code

```python3
class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            if nums[left] < nums[right]:
                return nums[left]
            mid = (left + right) // 2
            if nums[mid] < nums[right]:
                right = mid
            else:
                left = mid + 1
        return nums[left]
    
```
