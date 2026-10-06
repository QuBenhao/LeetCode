# [Python] Binary search

> Author: Benhao
> Date: 2021-06-14
> Upvotes: 5
> Tags: Python, Python3

---

### Approach
Find the peak in a given mountain array:
To the left of the peak, arr[i] < arr[i+1]
To the right of the peak, arr[i] > arr[i+1]

### Code

```python3
class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        n = len(arr)
        left, right = 1, n - 2
        while left < right:
            mid = (left + right) // 2
            if arr[mid] < arr[mid+1]:
                left = mid + 1
            else:
                right = mid
        return left

```
