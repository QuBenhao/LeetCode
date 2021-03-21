import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.setZeroes([x[:] for x in test_input])

    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])
        set_first_zero = 0 in matrix[0]

        for row in range(1,m):
            for col in range(n):
                if not matrix[row][col]:
                    matrix[0][col] = 0
                    matrix[row][0] = 0

        for row in range(1, m):
            for col in range(n-1,-1,-1):
                if not matrix[row][0] or not matrix[0][col]:
                    matrix[row][col] = 0

        if set_first_zero:
            for col in range(n):
                matrix[0][col] = 0

        return matrix
