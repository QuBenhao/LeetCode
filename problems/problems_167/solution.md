# [Python] Two pointers

> slug: python-shuang-zhi-zhen-by-himymben-uiap
> date: 2024-03-01
> tags: C, Java, Python, Python3, TypeScript
> question: Two Sum II - Input Array Is Sorted (two-sum-ii-input-array-is-sorted)
> url: https://leetcode.cn/problems/two-sum-ii-input-array-is-sorted/solutions/PwRPPJ/python-shuang-zhi-zhen-by-himymben-uiap/

---

> Problem: [167. 两数之和 II - 输入有序数组](https://leetcode.cn/problems/two-sum-ii-input-array-is-sorted/description/)

[TOC]

# Intuition

> To find a pair summing to target in a sorted array, move the pointers to increase or decrease the current sum according to its difference from the target.

# Approach

> Two pointers

# Complexity

Time complexity:
> $O(n)$

Space complexity:
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
  
