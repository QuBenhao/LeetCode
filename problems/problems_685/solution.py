import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.findRedundantDirectedConnection(test_input)

    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        # Update and return the representative of the node numbered x
        def find(x: int) -> int:
            # Return immediately if x is already the root
            # Otherwise, keep following parent links toward the root
            if x == pa[x]:
                return x
            pa[x] = find(pa[x])
            return pa[x]

        # Merge the sets containing the two nodes
        def unit(x: int, y: int):
            # Make y's representative the parent of x's representative
            # Attach the subtree containing x to the root of the subtree containing y
            pa[find(x)] = find(y)

        n = len(edges)
        pa = list(range(n + 1))  # pa[i] is node i's union-find parent; initially pa[i]=i, so each node is its own root
        fa = list(range(n + 1))  # fa[i] is node i's parent; initially fa[i]=i, so each node is its own parent

        conflict = -1  # Index of the conflicting edge; -1 initially means no conflict
        circle = -1  # Index of the cycle-forming edge; -1 initially means no cycle
        for i, (a, b) in enumerate(edges):
            if fa[b] != b:
                conflict = i  # Found a conflicting edge; do not add it to union-find
            else:
                fa[b] = a  # Record a as the parent of b
                if find(a) != find(b):
                    unit(a, b)  # Merge the nodes if they belong to different trees
                else:
                    circle = i  # If they already belong to the same tree, this edge is the last one forming the cycle

        if conflict < 0:
            return edges[circle]  # Cycle without conflict: return the last edge forming the cycle
        if circle < 0:
            return edges[conflict]  # Conflict without a cycle: remove the conflicting edge
        b = edges[conflict][1]
        return [fa[b], b]  # Both cycle and conflict: the other conflicting edge must be on the cycle, so remove it
