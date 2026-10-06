# [Python] Hash table / fast and slow pointers

> Author: Benhao
> Date: 2024-03-23
> Upvotes: 1
> Tags: C, Go, Java, Python3, TypeScript

---


> Problem: [202. 快乐数](https://leetcode.cn/problems/happy-number/description/)

[TOC]

# Intuition

> As with detecting a cycle in a linked list, use a hash table to record visited values, or check whether fast and slow pointers meet.

# Approach

> Hash table, fast and slow pointers

# Code
Hash table
```Python3 []
class Solution:
    def isHappy(self, n: int) -> bool:
        explored = {n}
        while n > 1:
            nxt = 0
            while n:
                nxt += (n % 10) ** 2
                n //= 10
            if nxt in explored:
                return False
            explored.add(nxt)
            n = nxt
        return True
```
Fast and slow pointers
```Python3 []
class Solution:
    def isHappy(self, n: int) -> bool:
        @lru_cache(None)
        def helper(x: int) -> int:
            res = 0
            while x:
                x, y = divmod(x, 10)
                res += y * y
            return res

        fast = slow = n
        while fast > 1:
            fast = helper(helper(fast))
            slow = helper(slow)
            if fast > 1 and fast == slow:
                return False
        return True
```
