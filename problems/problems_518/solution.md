# [Python] 动态规划

> Author: Benhao
> Date: 2024-03-25
> Upvotes: 1
> Tags: C, Go, Java, Python3, TypeScript

---


> Problem: [518. 零钱兑换 II](https://leetcode.cn/problems/coin-change-ii/description/)

[TOC]

# 思路

> 当前的取法由取这个硬币前的取法数目构成，符合递推

# 解题方法

> 动态规划，注意按金币的外循环，递推的内循环，这是为了组合数而不是排列数，也就是避免出现先取金币a、后取金币b，先取金币b、后取金币a的重复计算

# 复杂度

时间复杂度:
> $O(n)$

空间复杂度:
> $O(n)$



# Code
```Python3 []
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1
        for c in coins:
            for i in range(c, amount + 1):
                dp[i] += dp[i - c]
        return dp[-1]
```
  
