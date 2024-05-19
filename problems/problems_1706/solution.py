import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.findBall([x[:] for x in test_input])

    def findBall(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[int]
        """
        m = len(grid)
        n = len(grid[0])

        def dropball(row, col):
            if row == m:
                return col
            ang = grid[row][col]
            if (col == 0 and ang == -1) or (col == n - 1 and ang == 1) or (grid[row][col + ang] != ang):
                return -1

            return dropball(row + 1, col + ang)

        return [dropball(0, i) for i in range(n)]
