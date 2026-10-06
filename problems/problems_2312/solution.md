# [Python] DP / memoized search

> slug: python-dpji-yi-hua-sou-suo-by-himymben-j6eb
> date: 2024-03-15
> tags: C, Go, Java, Python3, TypeScript
> question: Selling Pieces of Wood (selling-pieces-of-wood)
> url: https://leetcode.cn/problems/selling-pieces-of-wood/solutions/7ZiV7z/python-dpji-yi-hua-sou-suo-by-himymben-j6eb/

---

> Problem: [2312. 卖木头块](https://leetcode.cn/problems/selling-pieces-of-wood/description/)

[TOC]

# Intuition

> The recursion is straightforward: the maximum value of the current piece is the best result over all possible cuts.

# Approach

> Pitfall 1: recursively enumerate cuts using prices. The long prices array causes too many recursive calls and a timeout. Here is the code that times out.
```Python3 []
        # This times out!!!!! Do not copy this code!!!
        @lru_cache(None)
        def dfs(i, j):
            return max(max(dfs(i - h, j) + dfs(h, j - w), dfs(i, j - w) + dfs(i - h, w)) + p if i >= h and j >= w else 0 for h, w, p in prices)

        # This times out!!!!! Do not copy this code!!!
        return dfs(m, n)
```
> Iterating over prices times out. Looking again at the constraints, m and n are small, so enumerate horizontal and vertical cuts directly.
> Pitfall 2: a piece whose dimensions occur in prices does not necessarily have its maximum value there; further cuts may earn more. Do not return immediately on a prices match: compare it with the values from cutting.
```Python3 []
        # This is incorrect!!!!! Do not copy this code!!!
        pd = {(h, w): p for h, w, p in prices}

        @lru_cache(None)
        def dfs(i, j):
            if (i, j) in pd:
                return pd[(i, j)]
            ans = 0
            for ni in range(1, i // 2 + 1):
                ans = max(ans, dfs(ni, j) + dfs(i - ni, j))
            for nj in range(1, j // 2 + 1):
                ans = max(ans, dfs(i, nj) + dfs(i, j - nj))
            return ans
        
        # This is incorrect!!!!! Do not copy this code!!!
        return dfs(m, n)
```
> Enumerate only half the horizontal and vertical cut positions, since j and n-j are symmetric.

# Complexity

Time complexity:
> $O(mn(m + n))$

Space complexity:
> $O(mn)$



# Code
```Python3 []
class Solution:
    def sellingWood(self, m: int, n: int, prices: List[List[int]]) -> int:
        pd = {(h, w): p for h, w, p in prices}

        @lru_cache(None)
        def dfs(i, j):             
            ans = pd.get((i, j), 0)
            for ni in range(1, i // 2 + 1):
                ans = max(ans, dfs(ni, j) + dfs(i - ni, j))
            for nj in range(1, j // 2 + 1):
                ans = max(ans, dfs(i, nj) + dfs(i, j - nj))
            return ans
        
        return dfs(m, n)
```
  
