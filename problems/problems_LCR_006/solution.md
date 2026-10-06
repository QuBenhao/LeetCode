# [Python] Two pointers

> slug: python-shuang-zhi-zhen-by-himymben-8ci6
> date: 2022-03-14
> tags: Python, Python3
> question: 两数之和 II - 输入有序数组 (kLl5u1)
> url: https://leetcode.cn/problems/kLl5u1/solutions/QhewVz/python-shuang-zhi-zhen-by-himymben-8ci6/

---
### Code

```python3
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, min(len(numbers) - 1, bisect_right(numbers, target))
        while l < r:
            if numbers[l] + numbers[r] == target:
                return [l, r]
            elif numbers[l] + numbers[r] > target:
                r -= 1
            else:
                l += 1
        return [l, r]
```
