import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        matrix, target = test_input
        return self.searchMatrix([x[:] for x in matrix], target)

    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        m, n = len(matrix), len(matrix[0])

        def search_row(col):
            left, right = 0, m
            while left < right:
                mid = (left + right) // 2
                if matrix[mid][col] == target:
                    return True
                elif matrix[mid][col] < target:
                    left = mid + 1
                else:
                    right = mid
            return left

        def search_col(row):
            left, right = 0, n
            while left < right:
                mid = (left + right) // 2
                if matrix[row][mid] == target:
                    return True
                elif matrix[row][mid] > target:
                    right = mid
                else:
                    left = mid + 1
            return False

        lowest_row = search_row(-1)
        if lowest_row is True:
            return True
        highest_row = search_row(0)
        if highest_row is True:
            return True
        for i in range(lowest_row, highest_row):
            if search_col(i):
                return True
        return False

        # m, n = len(matrix), len(matrix) and len(matrix[0])
        # r, c = 0, n - 1
        # while r < m and c >= 0:
        #     if target > matrix[r][c]:
        #         r += 1
        #     elif target < matrix[r][c]:
        #         c -= 1
        #     else:
        #         return True
        # return False
