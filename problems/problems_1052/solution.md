# [Python] 滑动窗口

> Author: Benhao
> Date: 2024-04-23
> Upvotes: 1
> Tags: C, Go, Java, Python3, TypeScript

---


> Problem: [1052. 爱生气的书店老板](https://leetcode.cn/problems/grumpy-bookstore-owner/description/)

[TOC]

# 思路

> 滑动窗口

# 解题方法

> 维护一个minutes窗口内全部满意

# 复杂度

时间复杂度:
> $O(n)$

空间复杂度:
> $O(1)$



# Code
```Python3 []
class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        total = cur = ans = 0
        for i, (c, g) in enumerate(zip(customers, grumpy)):
            if g:
                cur += c
            else:
                total += c
            if i >= minutes:
                if grumpy[i - minutes]:
                    cur -= customers[i - minutes]
                ans = max(ans, cur)
            else:
                ans = cur
        return ans + total
```
  
