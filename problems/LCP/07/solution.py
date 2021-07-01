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

        # k轮从0到n-1,相当于k-1轮从0能到达的地方到达n-1...
        # 递归关系为player的前置玩家们的传递
        # dp[k][player] = sum(dp[k-1][p']) for p' in graph[player]
        dp = [0] * n
        # 初始不需要任何传递玩家0就有信息
        dp[0] = 1
        for i in range(k):
            new_dp = [0] * n
            for j in range(n):
                # 所有能传到j的
                new_dp[j] += sum(dp[l] for l in graph[j])
            dp = new_dp
        return dp[n-1]
