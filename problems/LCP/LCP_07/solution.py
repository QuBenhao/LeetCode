import solution
from collections import defaultdict


class Solution(solution.Solution):
    def solve(self, test_input=None):
        n, relation, k = test_input
        return self.numWays(n, [x[:] for x in relation], k)

    def numWays(self, n, relation, k):
        """
        :type n: int
        :type relation: List[List[int]]
        :type k: int
        :rtype: int
        """
        graph = defaultdict(set)
        for a,b in relation:
            graph[b].add(a)

        # Reaching n-1 from 0 in k rounds means reaching a predecessor of n-1 from 0 in k-1 rounds...
        # The recurrence sums transmissions from the predecessors of player
        # dp[k][player] = sum(dp[k-1][p']) for p' in graph[player]
        dp = [0] * n
        # Initially, player 0 has the message without any transmissions
        dp[0] = 1
        for i in range(k):
            new_dp = [0] * n
            for j in range(n):
                # All players that can transmit to j
                new_dp[j] += sum(dp[l] for l in graph[j])
            dp = new_dp
        return dp[n-1]
