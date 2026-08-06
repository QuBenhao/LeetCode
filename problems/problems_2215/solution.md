# [Python] 集合差集 

> slug: python-by-himymben-tbto
> date: 2022-03-27
> tags: Python, Python3
> question: Find the Difference of Two Arrays (find-the-difference-of-two-arrays)
> url: https://leetcode.cn/problems/find-the-difference-of-two-arrays/solutions/FfjMGy/python-by-himymben-tbto/

---
### 代码

```python3
class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        return [list((s1 := set(nums1)) - (s2 := set(nums2))), list(s2 - s1)]
```