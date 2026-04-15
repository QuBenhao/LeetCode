# [Python] 记忆化搜索/二进制BFS

> Author: Benhao
> Date: 2024-03-24
> Upvotes: 1
> Tags: C, Go, Java, Python3, TypeScript

---


> Problem: [322. 零钱兑换](https://leetcode.cn/problems/coin-change/description/)

[TOC]

# 思路

> 取了一个钱，这个问题就变成取钱后的最小取钱方式，标准的递归题目

# 解题方法

> 记忆化搜索（动态规划）
> 这里提一下二进制转换，$a+b+c=x$求解可以转化为$2^a*2^b*2^c=2^x$，也就是$1 << x = 1 << a << b << c$
> 题目可以转化为：我们的取硬币操作可以理解为右移操作，取的总数变为$1<<amount$，我们最少需要右移多少次直到最小位出现1，也就是我们找到了取$1<<0$的路径了。这个时候其他位是不是1不影响，只要有一个路径出现就代表找到了。
> 在BFS的同时遍历coins进行右移，模拟取的操作，取了a以后下一次要取的数就变为$(1<<x)>>a$，重复这样的BFS

# 复杂度

时间复杂度:
> $O(n)$

空间复杂度:
> 记忆化$O(n)$
> 二进制BFS$O(1)$



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
  
