# [Python] Dijkstra

> slug: python-dijkstra-by-himymben-6xp9
> date: 2024-03-05
> tags: C, Go, Java, Python3, TypeScript
> question: Number of Ways to Arrive at Destination (number-of-ways-to-arrive-at-destination)
> url: https://leetcode.cn/problems/number-of-ways-to-arrive-at-destination/solutions/SyvYPh/python-dijkstra-by-himymben-6xp9/

---

> Problem: [1976. 到达目的地的方案数](https://leetcode.cn/problems/number-of-ways-to-arrive-at-destination/description/)

[TOC]

# 思路

> 以当前最小的距离消耗不停移动，叠加更新可以走到的次数，如果有更小的距离方案，则更新数目；如果是一致的距离方案，则叠加数目

# 解题方法

> 实际上是优先队列实现的Dijkstra算法


# Code
```Python3 []
MOD = int(1e9) + 7
class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        edges = [[] for _ in range(n)]
        for u, v, dis in roads:
            edges[u].append((v, dis))
            edges[v].append((u, dis))
        dists = [inf] * n
        cnts = [0] * n
        cnts[0] = 1
        pq = [(0, 0)]
        while pq:
            dis, node = heapq.heappop(pq)
            if dis > dists[node]:
                continue
            dists[node] = dis
            for other, cost in edges[node]:
                if (nxt := cost + dis) < dists[other]:
                    dists[other] = nxt
                    cnts[other] = cnts[node]
                    heapq.heappush(pq, (nxt, other))
                elif nxt == dists[other]:
                    cnts[other] = (cnts[other] + cnts[node]) % MOD
        return cnts[n - 1]
```
  
