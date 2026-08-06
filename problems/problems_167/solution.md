# [Python] 双指针

> slug: python-shuang-zhi-zhen-by-himymben-uiap
> date: 2024-03-01
> tags: C, Java, Python, Python3, TypeScript
> question: Two Sum II - Input Array Is Sorted (two-sum-ii-input-array-is-sorted)
> url: https://leetcode.cn/problems/two-sum-ii-input-array-is-sorted/solutions/PwRPPJ/python-shuang-zhi-zhen-by-himymben-uiap/

---

> Problem: [167. 两数之和 II - 输入有序数组](https://leetcode.cn/problems/two-sum-ii-input-array-is-sorted/description/)

[TOC]

# 思路

> 在有序的数组中找和为target的，根据当前和与目标的差异移动指针调整大小即可

# 解题方法

> 双指针

# 复杂度

时间复杂度:
> $O(n)$

空间复杂度:
> $O(1)$



# Code
```Python3 []
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1
        while left < right:
            if (s := numbers[left] + numbers[right]) == target:
                return [left + 1, right + 1]
            elif s < target:
                left += 1
            else:
                right -= 1
        return [-1, -1]
```
  
