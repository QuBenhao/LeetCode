from collections import defaultdict

import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.interactionCosts(*test_input)

    def interactionCosts(self, n: int, edges: List[List[int]], group: List[int]) -> int:
        graph = [[] for _ in range(n)]
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        ans = 0
        def dfs(node, pa):
            nonlocal ans
            cur = defaultdict(lambda: [0, 0])
            for child in graph[node]:
                if child != pa:
                    child_dict = dfs(child, node)
                    for k, v in child_dict.items():
                        # Moving from the subtree to the current node adds 1 to each node's distance, so add the node count
                        v[1] += v[0]
                        # Add this group's final contribution to the answer; these paths bend through the current node.
                        if cur[k][0]:
                            ans += cur[k][1] * v[0] + cur[k][0] * v[1]
                        # Merge into the current node's counts
                        cur[k][0] += v[0]
                        cur[k][1] += v[1]
            # Sum of contributions from pairing the current node with all subtrees
            ans += cur[group[node]][1]
            # Add the current node to its group's counts
            cur[group[node]][0] += 1
            return cur

        dfs(0, -1)
        return ans
