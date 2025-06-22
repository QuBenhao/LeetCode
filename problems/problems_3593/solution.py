from typing import *

import solution


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
            max_count, other_count = 0, 0
            for child in tree[node]:
                if child == parent:
                    continue
                child_sum, child_cost = dfs(child, node)
                if child_sum > cur_sum:
                    cur_sum = child_sum
                    other_count += max_count
                    max_count = 1
                elif child_sum == cur_sum:
                    max_count += 1
                else:
                    other_count += 1
                cur_cost += child_cost
            cur_cost += other_count
            cur_sum += cost[node]
            return cur_sum, cur_cost

        return dfs(0, 0)[1]
