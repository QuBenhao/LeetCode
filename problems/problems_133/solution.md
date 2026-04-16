# [Python] DFS

> Author: Benhao
> Date: 2024-03-21
> Upvotes: 2
> Tags: C, Go, Java, Python3, TypeScript

---


> Problem: [133. 克隆图](https://leetcode.cn/problems/clone-graph/description/)

[TOC]

# 思路

> 复制图

# 解题方法

> DFS遍历图同时记录走过的点

# 复杂度

时间复杂度:
> $O(n)$

空间复杂度:
> $O(n)$



# Code
```Python3 []
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else [] 
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        explored = {}

        def dfs(nd: Node, neigh_clone: Optional[Node]):
            clone_nd = Node(nd.val)
            explored[nd.val] = clone_nd
            if neigh_clone:
                neigh_clone.neighbors.append(clone_nd)
            for neighbor in nd.neighbors:
                if neighbor.val in explored:
                    clone_nd.neighbors.append(explored[neighbor.val])
                else:
                    dfs(neighbor, clone_nd)

        dfs(node, None)

        return explored[node.val]
```
  
