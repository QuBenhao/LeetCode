# [Python] O(n)前后缀最小值

> Author: Benhao
> Date: 2024-03-29
> Upvotes: 0
> Tags: C, Go, Java, Python3, TypeScript

---


> Problem: [2908. 元素和最小的山形三元组 I](https://leetcode.cn/problems/minimum-sum-of-mountain-triplets-i/description/)

[TOC]

# 思路

> 类似前缀和，遍历统计前缀后缀的最小值变化，再遍历统计最小答案即可

# 解题方法

> 前后缀

# 复杂度

时间复杂度:
> $O(n)$

空间复杂度:
> $O(n)$



# Code
```Python3 []
class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        n = len(nums)
        left_min, right_min = [inf] * n, [inf] * n
        for i in range(n):
            left_min[i] = min(left_min[i - 1], nums[i])
            right_min[n - 1 - i] = min(right_min[min(n - i, n - 1)], nums[n - 1 - i])
        ans = inf
        for i in range(1, n - 1):
            if nums[i] > left_min[i - 1] and nums[i] > right_min[i + 1]:
                ans = min(ans, left_min[i - 1] + right_min[i + 1] + nums[i])
        return ans if ans != inf else -1
```
  
