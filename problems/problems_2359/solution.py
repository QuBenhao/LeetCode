import solution
from typing import *
from math import inf


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.closestMeetingNode(*test_input)

    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        n = len(edges)
        
        dis1 = [-1] * n
        dis2 = [-1] * n
        ref = (dis1, dis2)
        
        def dfs(node, i):
            d = 0
            while node != -1 and ref[i][node] == -1:
                ref[i][node] = d
                node = edges[node]
                d += 1
        
        dfs(node1, 0)
        dfs(node2, 1)
        ans, ans_dis = -1, inf
        for i, (a, b) in enumerate(zip(dis1, dis2)):
            if a == -1 or b == -1:
                continue
            if (d := max(a, b)) < ans_dis:
                ans_dis = d
                ans = i
        return ans
