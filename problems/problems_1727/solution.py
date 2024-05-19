import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.largestSubmatrix([x[:] for x in test_input])

    def largestSubmatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        ans = 0
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col] != 0 and row > 0:
                    matrix[row][col] += matrix[row - 1][col]

            curr = sorted(matrix[row], reverse=True)
            for i in range(len(matrix[0])):
                ans = max(ans, curr[i] * (i + 1))

        return ans
