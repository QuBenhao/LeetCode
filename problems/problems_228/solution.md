# [Python] Range simulation

> Author: Benhao
> Date: 2024-03-01
> Upvotes: 7
> Tags: C, Go, Java, Python3, TypeScript

---


> Problem: [228. 汇总区间](https://leetcode.cn/problems/summary-ranges/description/)

[TOC]

# Intuition

> Move a pointer forward to determine the current range until all ranges have been traversed.

# Approach

> While each next element is one greater than the current element, advance to find the end of the current range. If the endpoint is the starting point, add that value alone; otherwise, add both endpoints.

# Complexity

Time complexity:
> $O(n)$

Space complexity:
> $O(n)$



# Code
```Python3 []
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ans, idx = [], 0
        while idx < len(nums):
            forward = idx + 1
            while forward < len(nums) and nums[forward] == nums[forward - 1] + 1:
                forward += 1
            if forward > idx + 1:
                ans.append(f"{nums[idx]}->{nums[forward - 1]}")
            else:
                ans.append(f"{nums[idx]}")
            idx = forward
        return ans
```
  
