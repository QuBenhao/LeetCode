# [Python] 滑动窗口

> Author: Benhao
> Date: 2024-03-01
> Upvotes: 4
> Tags: C, Go, Java, Python, Python3, TypeScript

---


> Problem: [209. 长度最小的子数组](https://leetcode.cn/problems/minimum-size-subarray-sum/description/)

[TOC]

# 思路

> 题目要找子数组而不是子序列，既然是连续的和，以滑动窗口处理找最小的窗口长度是最好的方法

# 解题方法

> 维护窗口和当前的和，如果已经满足条件从左边去除多余元素，比较窗口的大小

# 复杂度

时间复杂度:
> $O(n)$

空间复杂度:
> $O(n)$



# Code
```Python3 []
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        ans, cur = inf, 0
        window = deque([])
        for num in nums:
            cur += num
            window.append(num)
            while cur >= target:
                ans = min(ans, len(window))
                cur -= window.popleft()
        return ans if ans != inf else 0
```
  
