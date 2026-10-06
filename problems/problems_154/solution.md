# [Python] Binary search

> Author: Benhao
> Date: 2021-04-09
> Upvotes: 1
> Tags: Python, Python3

---

### Approach
If mid is smaller than right, the rotation point is at mid or to its left;
If mid is greater than right, the rotation point is to the right of mid;
If mid equals right, removing right does not affect the result. (To ensure the resulting index is at the rotation point, compare right with its left neighbor.)

### Code

```python3
class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] < nums[right]:
                right = mid
            elif nums[mid] > nums[right]:
                left = mid + 1
            else:
                if right and nums[right - 1] > nums[right]:
                    left = right
                else:
                    right -= 1
        return nums[left]

```
