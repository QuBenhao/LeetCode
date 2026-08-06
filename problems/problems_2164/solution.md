# [Python] 模拟

> slug: python-mo-ni-by-himymben-ev48
> date: 2022-02-06
> tags: Python, Python3
> question: Sort Even and Odd Indices Independently (sort-even-and-odd-indices-independently)
> url: https://leetcode.cn/problems/sort-even-and-odd-indices-independently/solutions/AAIVC3/python-mo-ni-by-himymben-ev48/

---
### 解题思路
按题目说的排序即可

### 代码

```python3
class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        nums[::2] = sorted(nums[::2])
        nums[1::2] = sorted(nums[1::2], reverse=True)
        return nums

```