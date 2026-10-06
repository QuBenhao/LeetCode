import solution
from collections import defaultdict


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.largestPathValue(*test_input)

    def largestPathValue(self, colors, edges):
        """
        :type colors: str
        :type edges: List[List[int]]
        :rtype: int
        """
        """
        Topological sort:
        Order all nodes in a directed graph so that no node points to a node before it.
        Compute each node's in-degree, remove nodes with in-degree 0, and decrement the in-degrees of their outgoing neighbors.
        Repeat until all nodes have been removed.
        If nodes remain but none has in-degree 0, the graph contains a cycle and has no topological ordering, which means many such problems have no solution.
        """
        n = len(colors)
        # In-degree of each node
        degree = [0] * n
        graph = defaultdict(set)
        for a,b in edges:
            degree[b] += 1
            graph[a].add(b)

        # dp: maximum count of each color on reaching each node
        dp = [[0] * 26 for _ in range(n)]
        # Topological sort
        q = [i for i in range(n) if not degree[i]]
        count = 0
        while q:
            count += 1
            i = q.pop()
            # Visit node i and add its color
            dp[i][ord(colors[i]) - ord('a')] += 1
            for j in graph[i]:
                degree[j] -= 1
                # Reach node j from node i; inherit each color count from i if it exceeds the current value
                for c in range(26):
                    dp[j][c] = max(dp[j][c], dp[i][c])
                if degree[j] == 0:
                    q.append(j)
        # Topological sorting detected a cycle
        if count != n:
            return -1
        return max(max(dp[i]) for i in range(n))
