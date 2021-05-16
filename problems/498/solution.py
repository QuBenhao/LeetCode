import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.findDiagonalOrder(test_input)

    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return []
        x, y = 0, 0
        res = []
        right = True
        m = len(matrix)
        n = len(matrix[0])
        while len(res) < m*n:
            res.append(matrix[x][y])
            if right:
                x -= 1
                y += 1
                if x < 0 or y == n:
                    right = False
                    if x < 0 and y < n:
                        x += 1
                    else:
                        x += 2
                        y -= 1
            else:
                x += 1
                y -= 1
                if x == m or y < 0:
                    right = True
                    if y < 0 and x < m:
                        y += 1
                    else:
                        y += 2
                        x -= 1
        return res
