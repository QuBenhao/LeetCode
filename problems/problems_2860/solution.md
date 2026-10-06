# [Python] Enumerate the number of selected students

> Author: Benhao
> Date: 2024-09-03
> Upvotes: 2
> Tags: Python3

---


> Problem: [2860. 让所有学生保持开心的分组方法数](https://leetcode.cn/problems/happy-students/description/)

[TOC]

# Intuition

> Enumerate the selected count in increasing order, selecting everyone whose value is smaller than that count. If the actual selected count matches the enumerated count, this is a valid answer.

# Solution steps

> Enumerate the selected count.

# Complexity

- $O(nlog_n)$



# Code
```Python3 []
class Solution:
    def countWays(self, nums: List[int]) -> int:
        ans = 0
        n = len(nums)
        nums.sort()
        cur, idx = 0, 0
        for i in range(n):
            while idx < n and nums[idx] < i:
                cur += 1
                idx += 1
            if idx < n and nums[idx] == i:
                cur += 1
                idx += 1
                continue
            if cur == i:
                ans += 1
        return ans + 1
```

A cleaner approach: if i students are selected, nums[i-1] and those before it are selected, while nums[i] and those after it are not. Count choices where i is strictly greater than nums[i-1] and strictly smaller than nums[i].
```Python3 []
class Solution:
    def countWays(self, nums: List[int]) -> int:
        nums.sort()
        # i people are selected: everyone at or below x is selected, and everyone at or above y is not
        return int(nums[0] > 0) + sum(x < i < y for i, (x, y) in enumerate(pairwise(nums), 1)) + 1
```
  
