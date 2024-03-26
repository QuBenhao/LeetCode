import solution
from typing import *
from object_libs import call_method
import heapq
from collections import defaultdict
from math import inf


class Solution(solution.Solution):
    def solve(self, test_input=None):
        ops, inputs = test_input
        obj = Graph(*inputs[0])
        return [None] + [call_method(obj, op, *ipt) for op, ipt in zip(ops[1:], inputs[1:])]


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
