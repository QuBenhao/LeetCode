# [Python] 数学

> slug: python-by-himymben-h4p5
> date: 2022-04-24
> tags: Python, Python3
> question: Check if an Array Is Consecutive (check-if-an-array-is-consecutive)
> url: https://leetcode.cn/problems/check-if-an-array-is-consecutive/solutions/UrQ8Zh/python-by-himymben-h4p5/

---
### 解题思路
满足题目条件只有一种情况，数组最大值比最小值大n-1 且 数组中无重复元素

### 代码

```python3
class Solution:
    def isConsecutive(self, nums: List[int]) -> bool:
        return max(nums) - min(nums) + 1 == len(nums) and len(set(nums)) == len(nums)
```