import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.reverse(test_input)

    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        ans, sign, num, INT_MAX = 0, 1 if x >=0 else -1, abs(x), (2 ** 31 - 1) // 10 if x > 0 else 2 ** 31 // 10
        while num:
            if ans > INT_MAX:
                return 0
            ans = ans * 10 + num % 10
            num //= 10
        return ans * sign

        # INT_MIN, INT_MAX = -2 ** 31 // 10 + 1, (2 ** 31 - 1) // 10
        # ans = 0
        # while x != 0:
        #     if ans > INT_MAX or ans < INT_MIN:
        #         return 0
        #     # Python3 的取模运算在 x 为负数时也会返回 [0, 9] 以内的结果，因此这里需要进行特殊判断
        #     digit = x % 10
        #     if x < 0 and digit > 0:
        #         digit -= 10
        #     # 不直接除10主要是Python对于负数除10的结果特殊
        #     x = (x - digit) // 10
        #     ans = ans * 10 + digit
        # return ans
