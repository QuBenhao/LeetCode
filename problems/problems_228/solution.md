# [Python] 区间模拟

> Author: Benhao
> Date: 2024-03-01
> Upvotes: 7
> Tags: C, Go, Java, Python3, TypeScript

---


> Problem: [228. 汇总区间](https://leetcode.cn/problems/summary-ranges/description/)

[TOC]

# 思路

> 用指针往前移动，确定当前区间的范围，直到遍历出所有区间

# 解题方法

> 假如下一个元素比当前大一，就一直往前找到不比前一个元素大一的位置，即为当前区间终点。如果终点在自己，那么加入自身区间，否则加入两端区间即可

# 复杂度

时间复杂度:
> $O(n)$

空间复杂度:
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
  
