import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.stoneGameVII(test_input)

    def stoneGameVII(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        n = len(stones)
        dp = [[0 for i in range(n)] for i in range(n)]

        for i in range(1, n):
            stones[i] += stones[i - 1]
        stones.insert(0, 0)

        # stones : 5 3 1 4 2
        # sum of stones : 0 5 8 9 13 15
        # pop out 15 will get 13 - 0 points (pop out j = stones[j] - stones[i])
        # pop out 5 will get 15 - 5 points (pop out i = stones[j+1] - stones[i+1])
        for i in range(n - 2, -1, -1):
            for j in range(i + 1, n):
                # max between pop out j and pop out i
                # minus because the other player always choose its best strategy
                dp[i][j] = max(stones[j] - stones[i] - dp[i][j - 1], stones[j + 1] - stones[i + 1] - dp[i + 1][j])

        return dp[0][n - 1]
