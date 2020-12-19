import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.cherryPickup([g[:] for g in test_input])

    def cherryPickup(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows, cols = len(grid), len(grid[0])
        dp = [[0] * cols for _ in range(cols)]
        for row in range(rows - 1, -1, -1):
            temp = [[0] * cols for _ in range(cols)]
            for i in range(cols - 1):
                for j in range(i, cols):
                    # For each (i, j) position in a row
                    for idx_i in (i - 1, i, i + 1):
                        for idx_j in (j - 1, j, j + 1):
                            if idx_i >= 0 and idx_j <= cols - 1:
                                temp[i][j] = max(temp[i][j], dp[idx_i][idx_j])
                    temp[i][j] += grid[row][i] + (0 if i == j else grid[row][j])
            dp = temp
        return dp[0][-1]

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