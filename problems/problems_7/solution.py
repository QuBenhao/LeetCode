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
        #     # Python3 modulo returns a result in [0, 9] even when x is negative, so special handling is needed here
        #     digit = x % 10
        #     if x < 0 and digit > 0:
        #         digit -= 10
        #     # Avoid dividing directly by 10 because Python handles division of negative numbers by 10 differently
        #     x = (x - digit) // 10
        #     ans = ans * 10 + digit
        # return ans
