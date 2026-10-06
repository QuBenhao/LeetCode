# [Python] Mathematics

> slug: python-by-himymben-h4p5
> date: 2022-04-24
> tags: Python, Python3
> question: Check if an Array Is Consecutive (check-if-an-array-is-consecutive)
> url: https://leetcode.cn/problems/check-if-an-array-is-consecutive/solutions/UrQ8Zh/python-by-himymben-h4p5/

---
### Approach
The conditions hold exactly when the maximum exceeds the minimum by n-1 and the array has no duplicate elements.

### Code

```python3
class Solution:
    def isConsecutive(self, nums: List[int]) -> bool:
        return max(nums) - min(nums) + 1 == len(nums) and len(set(nums)) == len(nums)
```
