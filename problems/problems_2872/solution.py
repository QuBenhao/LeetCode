import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.maxKDivisibleComponents(*test_input)

    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        g = [[] for _ in range(n)]
        for x, y in edges:
            g[x].append(y)
            g[y].append(x)

        # Return the sum of node weights in the subtree rooted at x
        def dfs(x: int, fa: int) -> int:
            s = values[x]
            for y in g[x]:
                if y != fa:  # Avoid visiting the parent
                    # Add subtree y's node-weight sum to obtain subtree x's sum
                    s += dfs(y, x)
            nonlocal ans
            ans += s % k == 0
            return s

        ans = 0
        dfs(0, -1)
        return ans
