# [Python] 枚举被选人数

> Author: Benhao
> Date: 2024-09-03
> Upvotes: 2
> Tags: Python3

---


> Problem: [2860. 让所有学生保持开心的分组方法数](https://leetcode.cn/problems/happy-students/description/)

[TOC]

# 思路

> 从小到大枚举被选人数，把小于被选人数的都选出来，如果选中的人数和枚举的被选人数一致，那么这是可行的答案之一

# 解题过程

> 枚举选中人数

# 复杂度

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

或者更好的写法，当前选了i个人，那么nums[i-1]及以下就被选了，nums[i]及以上就没被选，我们统计满足严格大于nums[i-1]且严格小于nums[i]的数量即可
```Python3 []
class Solution:
    def countWays(self, nums: List[int]) -> int:
        nums.sort()
        # 当前选了i个人, x及以下的人都选了，y及以上的人都没选
        return int(nums[0] > 0) + sum(x < i < y for i, (x, y) in enumerate(pairwise(nums), 1)) + 1
```
  
