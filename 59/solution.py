import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.generateMatrix(test_input)

    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        ans = [[0] * n for _ in range(n)]
        i, j, di, dj = 0, 0, 0, 1
        for k in range(n * n):
            ans[i][j] = k + 1
            if ans[(i + di) % n][(j + dj) % n]:
                # 0, 1 -> 1, 0 -> 0, -1 -> -1, 0 -> 0, 1
                di, dj = dj, -di
            i += di
            j += dj
        return ans

        # def fill_ring(start, k, curr):
        #     x, y = start
        #     if k == 1:
        #         self.matrix[x][y] = curr
        #         return None,None
        #     for j in range(4):
        #         for i in range(k-1):
        #             self.matrix[x][y] = curr
        #             if j == 0:
        #                 y += 1
        #             elif j == 1:
        #                 x += 1
        #             elif j == 2:
        #                 y -= 1
        #             else:
        #                 x -= 1
        #             curr += 1
        #     return (x + 1, y + 1),curr
        #
        # self.matrix = [[0 for i in range(n)] for i in range(n)]
        # curr = 1
        # start = 0, 0
        # for i in range(n, 0, -2):
        #     start,curr = fill_ring(start, i, curr)
        # return self.matrix
