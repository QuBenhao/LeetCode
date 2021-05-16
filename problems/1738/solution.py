import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        matrix, k = test_input
        return self.kthLargestValue([x[:] for x in matrix], k)

    def kthLargestValue(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        m = len(matrix)
        n = len(matrix[0])
        xorl = []
        for i in range(m):
            for j in range(n):
                if j > 0:
                    matrix[i][j] ^= matrix[i][j-1]
                if i > 0:
                    matrix[i][j] ^= matrix[i-1][j]
                if i > 0 and j > 0:
                    matrix[i][j] ^= matrix[i-1][j-1]
                xorl.append(matrix[i][j])
        return sorted(xorl)[-k]
