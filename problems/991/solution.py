import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.brokenCalc(*test_input)

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
        # multiply 2 until X is greater than Y
        while X < Y:
            X *= 2
            count += 1
        # Currently, the result is count+left, which might not be optimal
        # Calculate when should we decrement 1 to save cost using toss and divide
        left = X - Y
        power = count
        while left > 0:
            # if left // 2 ** power > 0, this means we should minus 1 before multiply 2 at that level
            count += left // 2 ** power
            left %= 2 ** power
            power -= 1
        return count
