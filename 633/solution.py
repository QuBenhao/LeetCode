import solution
import math


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.judgeSquareSum(test_input)

    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        if not c:
            return True
        # (a - b) ^ 2 + (a + b) ^ 2 = 2 * (a ^ 2 + b ^ 2) = 2 * c
        while c % 2 == 0:
            c //= 2
        # 费马平方和定理
        if c % 4 == 3:
            return False
        for i in range(3, int(math.sqrt(c)) + 1, 4):
            count = 0
            while c % i == 0:
                c //= i
                count += 1
            if count % 2 != 0:
                return False
        return True

        # # 双指针解法
        # sqrt = int(math.sqrt(c))
        # if sqrt * sqrt == c:
        #     return True
        # # sqrt < math.sqrt(c)
        # i, j = 1, sqrt
        # while i <= j:
        #     res = i * i + j * j
        #     if res == c:
        #         return True
        #     elif res < c:
        #         i += 1
        #     else:
        #         j -= 1
        # return False
