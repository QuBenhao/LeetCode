# [Python] dijkstra

> Author: Benhao
> Date: 2024-03-26
> Upvotes: 1
> Tags: C, Go, Java, Python3, TypeScript

---


> Problem: [2642. 设计可以求最短路径的图类](https://leetcode.cn/problems/design-graph-with-shortest-path-calculator/description/)

[TOC]

# 思路

> dijkstra

# 解题方法

> 构图，在线查询


# Code
```Python3 []
class Graph:
    def __init__(self, n: int, edges: List[List[int]]):
        self.graph = defaultdict(list)
        for a, b, cost in edges:
            self.graph[a].append((b, cost))

    def addEdge(self, edge: List[int]) -> None:
        self.graph[edge[0]].append((edge[1], edge[2]))

    def shortestPath(self, node1: int, node2: int) -> int:
        dist = defaultdict(lambda: defaultdict(lambda: inf))
        pq = [(0, node1)]
        while pq:
            cur, node = heapq.heappop(pq)
            if node == node2:
                return cur
            for neighbor, cost in self.graph[node]:
                if (nxt := cur + cost) < dist[node][neighbor]:
                    heapq.heappush(pq, (nxt, neighbor))
                    dist[node][neighbor] = nxt
        return -1


# Your Graph object will be instantiated and called as such:
# obj = Graph(n, edges)
# obj.addEdge(edge)
# param_2 = obj.shortestPath(node1,node2)
```
  
