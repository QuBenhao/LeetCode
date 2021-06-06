import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        mat, target = test_input
        return self.findRotation([x[:] for x in mat], [x[:] for x in target])

    def findRotation(self, mat, target):
        """
        :type mat: List[List[int]]
        :type target: List[List[int]]
        :rtype: bool
        """
        def rotate(matrix):
            m, n = len(matrix), len(matrix[0])
            new = [[0] * m for _ in range(n)]
            for i in range(m):
                for j in range(n):
                    new[j][m - 1 - i] = matrix[i][j]
            return new

        if mat == target:
            return True

        for i in range(3):
            mat = rotate(mat)
            if mat == target:
                return True
        return False
