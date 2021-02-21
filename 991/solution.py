import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        X, Y = test_input
        return self.brokenCalc(X, Y)

    def brokenCalc(self, X, Y):
        """
        :type X: int
        :type Y: int
        :rtype: int
        """
        # return X - Y if X >= Y else self.brokenCalc(X, Y // 2 if Y % 2 == 0 else Y + 1) + 1

        if X >= Y:
            return X - Y

        count = 0
        N = 1
        while X * 2 ** N < Y:
            N += 1
        remain = (X * 2 ** N) - Y
        count += N
        while N >= 0:
            count += remain // (2 ** N)
            remain %= (2 ** N)
            N -= 1

        return count
