import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        N, mines = test_input
        return self.orderOfLargestPlusSign(N, mines)

    def orderOfLargestPlusSign(self, N, mines):
        """
        :type N: int
        :type mines: List[List[int]]
        :rtype: int
        """
        grid = [[N] * N for i in range(N)]

        for m in mines:
            grid[m[0]][m[1]] = 0

        for i in range(N):
            l, r, u, d = 0, 0, 0, 0

            for j, k in zip(range(N), reversed(range(N))):
                l = l + 1 if grid[i][j] != 0 else 0
                if l < grid[i][j]:
                    grid[i][j] = l

                r = r + 1 if grid[i][k] != 0 else 0
                if r < grid[i][k]:
                    grid[i][k] = r

                u = u + 1 if grid[j][i] != 0 else 0
                if u < grid[j][i]:
                    grid[j][i] = u

                d = d + 1 if grid[k][i] != 0 else 0
                if d < grid[k][i]:
                    grid[k][i] = d

        res = 0

        for i in range(N):
            for j in range(N):
                if res < grid[i][j]:
                    res = grid[i][j]

        return res

        # # Exceed time limit first solution
        # if len(mines) == N * N:
        #     return 0
        #
        # left = [[0 for i in range(N)] for i in range(N)]
        # up = [[0 for i in range(N)] for i in range(N)]
        # right = [[0 for i in range(N)] for i in range(N)]
        # down = [[0 for i in range(N)] for i in range(N)]
        # for i in range(N):
        #     for j in range(N):
        #         if j > 0:
        #             if [i, j - 1] not in mines:
        #                 left[i][j] = left[i][j - 1] + 1
        #             if [i, N - j] not in mines:
        #                 right[i][N - 1 - j] = right[i][N - j] + 1
        #         if i > 0:
        #             if [i - 1, j] not in mines:
        #                 up[i][j] = up[i - 1][j] + 1
        #             if [N - i, j] not in mines:
        #                 down[N - 1 - i][j] = down[N - i][j] + 1
        # largest = 0
        # for i in range(N):
        #     for j in range(N):
        #         if [i, j] in mines:
        #             continue
        #         curr = min(left[i][j], right[i][j], up[i][j], down[i][j])
        #         if curr > largest:
        #             largest = curr
        #
        # return largest + 1
