# [Python] DP/记忆化搜索

> slug: python-dpji-yi-hua-sou-suo-by-himymben-j6eb
> date: 2024-03-15
> tags: C, Go, Java, Python3, TypeScript
> question: Selling Pieces of Wood (selling-pieces-of-wood)
> url: https://leetcode.cn/problems/selling-pieces-of-wood/solutions/7ZiV7z/python-dpji-yi-hua-sou-suo-by-himymben-j6eb/

---

> Problem: [2312. 卖木头块](https://leetcode.cn/problems/selling-pieces-of-wood/description/)

[TOC]

# 思路

> 这题的递归比较好推理，就是当前块的最大价值由枚举不同割法的最大价值构成

# 解题方法

> 踩坑1：递归枚举prices切割，因prices数组长，递归次数多必然超时。超时代码
```Python3 []
        # 会超时！！！！！别CV这里!!!
        @lru_cache(None)
        def dfs(i, j):
            return max(max(dfs(i - h, j) + dfs(h, j - w), dfs(i, j - w) + dfs(i - h, w)) + p if i >= h and j >= w else 0 for h, w, p in prices)

        # 会超时！！！！！别CV这里!!!
        return dfs(m, n)
```
> 遍历prices会超时，重新观察数据范围，发现m和n小，那么直接枚举行和列的割法即可。
> 踩坑2: 如果当前行、列在prices内，不代表它是最大价值的，可能继续切割仍有更大价值，所以不能一在prices里就返回，仍要判断切割后对比最大值。
```Python3 []
        # 会错误！！！！！别CV这里!!!
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
        
        # 会错误！！！！！别CV这里!!!
        return dfs(m, n)
```
> 枚举当前行的一半割法、当前列的一半割法即可，因为j和n-j具有对称性

# 复杂度

时间复杂度:
> $O(mn(m + n))$

空间复杂度:
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
  
