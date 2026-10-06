# [Python] Dynamic programming

> Author: Benhao
> Date: 2024-03-25
> Upvotes: 1
> Tags: C, Go, Java, Python3, TypeScript

---


> Problem: [518. 零钱兑换 II](https://leetcode.cn/problems/coin-change-ii/description/)

[TOC]

# Intuition

> The number of ways to reach the current amount comes from the ways before taking this coin, which gives a recurrence.

# Approach

> Use dynamic programming with coins in the outer loop and the recurrence in the inner loop. This counts combinations rather than permutations, avoiding duplicate counts for taking coin a then coin b versus coin b then coin a.

# Complexity

Time complexity:
> $O(n)$

Space complexity:
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
  
