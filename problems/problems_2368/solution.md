# [Python] DFS

> slug: python-dfs-by-himymben-i2bg
> date: 2024-03-02
> tags: C, Go, Java, Python3, TypeScript
> question: Reachable Nodes With Restrictions (reachable-nodes-with-restrictions)
> url: https://leetcode.cn/problems/reachable-nodes-with-restrictions/solutions/gMmb9W/python-dfs-by-himymben-i2bg/

---

> Problem: [2368. 受限条件下可到达节点的数目](https://leetcode.cn/problems/reachable-nodes-with-restrictions/description/)

[TOC]

# 思路

> 直接从0开始dfs，遇到禁止点返回，直到递归完

# 解题方法

> DFS

# 复杂度

时间复杂度:
> $O(n)$

空间复杂度:
> $O(n)$



# Code
```Python3 []
class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        deadend = set(restricted)
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        def dfs(node, parent):
            if node in deadend:
                return 0
            return 1 + sum(dfs(child, node) if child != parent else 0 for child in graph[node])
        
        return dfs(0, -1)
```
  
