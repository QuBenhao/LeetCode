import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.concatenatedBinary(test_input)

    def concatenatedBinary(self, n):
        """
        :type n: int
        :rtype: int
        """

        def multiply(X, Y):
            return [[sum(a * b for a, b in zip(X_row, Y_col)) % 1000000007 for Y_col in zip(*Y)] for X_row in X]

        def x_level_k_product(x, k):
            res = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
            mat = [[2 ** k, 1, 0], [0, 1, 1], [0, 0, 1]]
            while x > 0:
                if x & 1: res = multiply(res, mat)
                mat, x = multiply(mat, mat), x >> 1
            return res

        ans, acc, level = [[1], [2], [1]], 1, 1
        while acc < n:
            next_level = 2 ** (level + 1)
            take = min(n, next_level - 1) - acc
            ans = multiply(x_level_k_product(take, level + 1), ans)
            acc, level = acc + take, level + 1

        return ans[0][0]
