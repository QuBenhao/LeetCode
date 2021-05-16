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

        # ans = [[0] * n for _ in range(n)]
        # x, y, curr = 0, 0, 1
        # while n > 1:
        #     for j in range(4):
        #         for i in range(n-1):
        #             ans[x][y] = curr
        #             if j == 0:
        #                 y += 1
        #             elif j == 1:
        #                 x += 1
        #             elif j == 2:
        #                 y -= 1
        #             else:
        #                 x -= 1
        #             curr += 1
        #     x += 1
        #     y += 1
        #     n -= 2
        # if n == 1:
        #     ans[x][y] = curr
        # return ans

        # ans = [[0] * n for _ in range(n)]
        # i, j, curr = 0, 0, 1
        # while n > 1:
        #     for j in range(j, j + n-1):
        #         ans[i][j] = curr
        #         curr += 1
        #     j += 1
        #     for i in range(i, i +n-1):
        #         ans[i][j] = curr
        #         curr += 1
        #     i += 1
        #     for j in range(j, j-n+1, -1):
        #         ans[i][j] = curr
        #         curr += 1
        #     j -= 1
        #     for i in range(i, i-n+1, -1):
        #         ans[i][j] = curr
        #         curr += 1
        #     j += 1
        #     n -= 2
        # if n == 1:
        #     ans[i][j] = curr
        # return ans
