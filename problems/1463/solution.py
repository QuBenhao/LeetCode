import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.cherryPickup([g[:] for g in test_input])

    def cherryPickup(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows = len(grid)
        cols = len(grid[0])
        dp = [[[grid[i][j] + grid[i][k] for k in range(cols)] for j in range(cols)] for i in range(rows)]
        for i in range(rows-2, -1, -1):
            for j in range(cols - 1):
                for k in range(j + 1, cols):
                    dp[i][j][k] += max([dp[i+1][l][r]
                                       for l in range(j-1,j+2)
                                       for r in range(k-1,k+2)
                                       if 0 <= l < r < cols])
        return dp[0][0][cols - 1]

        # m = len(grid)
        # n = len(grid[0])
        #
        # @lru_cache(None)
        # def dp(row, col1, col2):
        #     if col1 < 0 or col1 >= n or col2 < 0 or col2 >= n:
        #         return -inf
        #     # current cell
        #     result = 0
        #     result += grid[row][col1]
        #     if col1 != col2:
        #         result += grid[row][col2]
        #     # transition
        #     if row != m-1:
        #         result += max(dp(row+1, new_col1, new_col2)
        #                       for new_col1 in [col1, col1+1, col1-1]
        #                       for new_col2 in [col2, col2+1, col2-1])
        #     return result
        #
        # return dp(0, 0, n-1)
