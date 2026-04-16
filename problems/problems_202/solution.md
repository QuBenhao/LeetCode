# [Python] 哈希表/快慢指针

> Author: Benhao
> Date: 2024-03-23
> Upvotes: 1
> Tags: C, Go, Java, Python3, TypeScript

---


> Problem: [202. 快乐数](https://leetcode.cn/problems/happy-number/description/)

[TOC]

# 思路

> 和链表是否有环同理，可以用哈希记录，也可以用快慢指针是否会追上

# 解题方法

> 哈希表、快慢指针

# Code
哈希表
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
快慢指针
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
