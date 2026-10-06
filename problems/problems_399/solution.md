# [Python] Concise BFS

> Author: Benhao
> Date: 2024-03-28
> Upvotes: 13
> Tags: C, Go, Java, Python3, TypeScript

---


> Problem: [399. 除法求值](https://leetcode.cn/problems/evaluate-division/description/)

[TOC]

# Intuition

> equations defines state transitions: graph nodes and edges. values gives transition costs. queries asks whether a path exists from the starting state to the final state and what its cost is.

# Approach

> Standard BFS

# Complexity

Time complexity:
> $O(n)$

Space complexity:
> $O(n)$



# Code
```Python3 []
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)
        for (a, b), val in zip(equations, values):
            graph[a].append((b, val))
            graph[b].append((a, 1.0 / val))

        def bfs(init, goal):
            if init not in graph or goal not in graph:
                return -1.0
            explored = {init}
            q = deque([(init, 1.0)])
            while q:
                node, v = q.popleft()
                if node == goal:
                    return v
                for nxt, cost in graph[node]:
                    if nxt not in explored:
                        explored.add(nxt)
                        q.append((nxt, v * cost))
            return -1.0

        return [bfs(i, g) for i, g in queries]
```
  
