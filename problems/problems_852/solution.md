# [Python] 二分查找

> Author: Benhao
> Date: 2021-06-14
> Upvotes: 5
> Tags: Python, Python3

---

### 解题思路
给定山形数组找顶点，
顶点左边满足 arr[i] < arr[i+1]
顶点右边满足 arr[i] > arr[i+1]

### 代码

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