# [Python] 删除检测

> Author: Benhao
> Date: 2021-06-27
> Upvotes: 6
> Tags: Python, Python3

---

### 解题思路
当时觉得一道简单题为什么要想那么麻烦，于是就写出了这个。
分别删除第一个不满足递增的位置的两个，如果任意一个满足递增，那么为True
否则为False

### 代码

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