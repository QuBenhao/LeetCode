# [Python] 二分法

> Author: Benhao
> Date: 2021-04-09
> Upvotes: 1
> Tags: Python, Python3

---

### 解题思路
mid比right小，断点在mid及其左侧；
mid比right大，断点在mid右侧；
mid和right相等，去掉right不会影响结果。（为了避免结果的index不是断点处，判断right和它左边的大小关系）

### 代码

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