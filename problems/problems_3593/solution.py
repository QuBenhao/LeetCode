from collections import defaultdict

import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.minIncrease(*test_input)

    def minIncrease(self, n: int, edges: List[List[int]], cost: List[int]) -> int:
        tree = [[] for _ in range(n)]
        for u, v in edges:
            tree[u].append(v)
            tree[v].append(u)

        def dfs(node, parent):
            cur_sum, cur_cost = 0, 0
            counter = defaultdict(int)
            for child in tree[node]:
                if child == parent:
                    continue
                child_sum, child_cost = dfs(child, node)
                counter[child_sum] += 1
                cur_sum = max(cur_sum, child_sum)
                cur_cost += child_cost
            for k, v in counter.items():
                if k != cur_sum:
                    cur_cost += v
            cur_sum += cost[node]
            return cur_sum, cur_cost

        return dfs(0, 0)[1]
