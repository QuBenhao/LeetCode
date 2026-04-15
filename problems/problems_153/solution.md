# [Python] 二分查找断点

> Author: Benhao
> Date: 2021-04-08
> Upvotes: 1
> Tags: Python, Python3

---

### 解题思路
如果left比right小，那么left就是left到right的最小值;
如果mid比right小，那么断点就在mid或者mid左边，比如[5,1,2,3,4]，`right = 4`,`mid = 2`,最小值在mid左侧。
如果mid比left大，那么断电就在mid右边，比如[3,4,5,1,2],`left = 3`,`mid = 5`,最小值在mid右侧。
**不存在nums[right]<nums[mid]<nums[left]**

### 代码

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