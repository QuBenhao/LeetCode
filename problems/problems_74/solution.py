import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.searchMatrix(*test_input)

    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        m, n = len(matrix), len(matrix[0])

        def row_binary_search(val):
            left, right = 0, m - 1
            while left < right:
                mid = (left + right) // 2
                if val == matrix[mid][0] or val == matrix[mid][-1]:
                    return True
                elif val < matrix[mid][0]:
                    right = mid - 1
                elif val > matrix[mid][-1]:
                    left = mid + 1
                else:
                    return mid
            return left

        def col_binary_search(row, val):
            left, right = 0, n - 1
            while left <= right:
                mid = (left + right) // 2
                if val == matrix[row][mid]:
                    return True
                elif val > matrix[row][mid]:
                    left = mid + 1
                else:
                    right = mid - 1
            return False

        r = row_binary_search(target)
        if type(r) == bool:
            return r
        return col_binary_search(r, target)

        # m, n = len(matrix), len(matrix[0])
        # x, y = m - 1, 0
        # while x >= 0 and y < n:
        #     if matrix[x][y] == target:
        #         return True
        #     elif matrix[x][y] > target:
        #         x -= 1
        #     else:
        #         y += 1
        # return False
