# [Python] Memoized search / binary BFS

> Author: Benhao
> Date: 2024-03-24
> Upvotes: 1
> Tags: C, Go, Java, Python3, TypeScript

---


> Problem: [322. 零钱兑换](https://leetcode.cn/problems/coin-change/description/)

[TOC]

# Intuition

> After taking one coin, the problem becomes finding the minimum number of coins for the remaining amount: a standard recursive problem.

# Approach

> Memoized search (dynamic programming)
> A note on the binary transformation: solving $a+b+c=x$ can be transformed into $2^a*2^b*2^c=2^x$, or $1 << x = 1 << a << b << c$.
> Reframe taking a coin as a right shift, with the total represented by $1<<amount$. Find the fewest right shifts needed for a 1 to appear in the lowest bit, meaning a path to $1<<0$ has been found. Whether other bits are 1 does not matter; one such path is enough.
> During BFS, iterate over coins and shift right to simulate taking each coin. After taking a, the next state is $(1<<x)>>a$. Repeat this BFS.

# Complexity

Time complexity:
> $O(n)$

Space complexity:
> Memoization $O(n)$
> Binary BFS $O(1)$



# Code
```Python3 []
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        @lru_cache(None)
        def dfs(remain):
            return min(dfs(remain - c) for c in coins) + 1 if remain > 0 else (0 if not remain else inf)
        
        return -1 if (ans := dfs(amount)) == inf else ans
```
```Python3 []
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if not amount:
            return 0
        step, dp = 0, 1 << amount
        while dp:
            nxt = 0
            step += 1
            for c in coins:
                nxt |= dp >> c
            if nxt & 1:
                return step
            dp = nxt
        return -1
```
  
