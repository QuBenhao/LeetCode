import solution
from sortedcontainers import SortedList


class Solution(solution.Solution):
    def solve(self, test_input=None):
        matrix, k = test_input
        return self.maxSumSubmatrix([x[:] for x in matrix], k)

    def maxSumSubmatrix(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        # m, n = len(matrix), len(matrix[0])
        #
        # presum = [[0] * (n + 1) for _ in range(m + 1)]
        # for i in range(m):
        #     for j in range(n):
        #         presum[i + 1][j + 1] = presum[i][j + 1] + presum[i + 1][j] - presum[i][j] + matrix[i][j]
        #
        # ans = float("-inf")
        # for i in range(1, m + 1):
        #     for j in range(i, m + 1):
        #         ts = SortedList()
        #         ts.add(0)
        #         for r in range(1, n + 1):
        #             right = presum[j][r] - presum[i - 1][r]
        #             left = ts.bisect_left(right - k)
        #             if left < len(ts):
        #                 ans = max(ans, right - ts[left])
        #             ts.add(right)
        #
        # return ans

        m, n = len(matrix), len(matrix[0])
        isRight = n > m
        m, n = max(m, n), min(m, n)
        ans = float("-inf")
        for i in range(1, n + 1):
            presum = [0] * (m + 1)
            for j in range(i, n + 1):
                ts = SortedList()
                ts.add(0)
                a = 0
                for fixed in range(1, m + 1):
                    presum[fixed] += matrix[j - 1][fixed - 1] if isRight else matrix[fixed - 1][j - 1]
                    a += presum[fixed]
                    b = ts.bisect_left(a - k)
                    if b < len(ts):
                        ans = max(ans, a - ts[b])
                    ts.add(a)
        return ans
