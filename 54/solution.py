import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.spiralOrder(test_input)

    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        # from sys import version_info
        # if version_info.major < 3:
        #     return matrix and list(matrix.pop(0)) + self.spiralOrder(zip(*matrix)[::-1])
        # else:
        #     return matrix and [*matrix.pop(0)] + self.spiralOrder([*zip(*matrix)][::-1])

        ans = []
        m, n = len(matrix), len(matrix[0])
        left, top, right, down = 0, 0, n - 1, m - 1
        while left <= right and top <= down:
            for i in range(left, right):
                ans.append(matrix[top][i])
            if top == down:
                ans.append(matrix[top][right])
                break
            for i in range(top, down):
                ans.append(matrix[i][right])
            if left == right:
                ans.append(matrix[down][right])
                break
            for i in range(right, left, -1):
                ans.append(matrix[down][i])
            for i in range(down, top, -1):
                ans.append(matrix[i][left])
            left += 1
            top += 1
            right -= 1
            down -= 1
        return ans

        # ans = []
        # m, n = len(matrix), len(matrix[0])
        # left, top, right, down = 0, 0, n - 1, m - 1
        # dir = 0
        # while left <= right and top <= down:
        #     if dir == 0:
        #         for i in range(left, right + 1):
        #             ans.append(matrix[top][i])
        #         top += 1
        #     elif dir == 1:
        #         for i in range(top, down + 1):
        #             ans.append(matrix[i][right])
        #         right -= 1
        #     elif dir == 2:
        #         for i in range(right, left - 1, -1):
        #             ans.append(matrix[down][i])
        #         down -= 1
        #     else:
        #         for i in range(down, top - 1, -1):
        #             ans.append(matrix[i][left])
        #         left += 1
        #     dir = (dir + 1) % 4
        # return ans
