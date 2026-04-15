# [Python] 拓扑排序

> Author: Benhao
> Date: 2024-04-03
> Upvotes: 3
> Tags: C, Go, Java, Python3, TypeScript

---


> Problem: [2192. 有向无环图中一个节点的所有祖先](https://leetcode.cn/problems/all-ancestors-of-a-node-in-a-directed-acyclic-graph/description/)

[TOC]

# 思路

> 以拓扑排序可以统计干净遍历到的节点的所有祖先，因为遍历到它时它的入度为0，说明所有祖先都已经处理过

# 解题方法

> 拓扑排序


# Code
```Python3 []
class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        from collections import defaultdict, deque
        graph, direct, ans = defaultdict(list), [0] * n, [set() for _ in range(n)]
        for a, b in edges:
            graph[a].append(b)
            direct[b] += 1
        q = deque([])
        for i in range(n):
            if direct[i] == 0:
                q.append(i)
        while q:
            node = q.popleft()
            for child in graph[node]:
                ans[child].update(ans[node])
                ans[child].add(node)
                direct[child] -= 1
                if direct[child] == 0:
                    q.append(child)
        return [list(sorted(s)) for s in ans]
```
  
