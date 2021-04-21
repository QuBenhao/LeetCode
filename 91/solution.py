import solution
from functools import lru_cache


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.numDecodings(str(test_input))

    @lru_cache(None)
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s and int(s[0]) == 0:
            return 0
        if len(s) <= 1:
            return 1
        if int(s[:2]) <= 26:
            return self.numDecodings(s[1:]) + self.numDecodings(s[2:])
        return self.numDecodings(s[1:])

        # str_list = []
        # start = end = 0
        # max_length = 0
        # for i, c in enumerate(s):
        #     if c == '0' or c >= '3':
        #         end = i
        #         str_list.append(s[start:end + 1])
        #         if len(str_list[-1]) > max_length:
        #             max_length = len(str_list[-1])
        #         if '0' in str_list:
        #             return 0
        #         start = end + 1
        #     else:
        #         end += 1
        #
        # if start != len(s):
        #     str_list.append(s[start:end+1])
        #     if len(str_list[-1]) > max_length:
        #         max_length = len(str_list[-1])
        #
        # count = 1
        # dp = [1] * max_length
        #
        # for i in range(max_length):
        #     if i == 1:
        #         dp[i] = 2
        #     if i > 1:
        #         dp[i] = dp[i - 1] + dp[i - 2]
        #
        # for s_ in str_list:
        #     if len(s_) == 1:
        #         continue
        #     if s_[-1] == '0':
        #         if len(s_) > 2:
        #             count *= dp[len(s_) - 3]
        #     elif s_[-1] > '6':
        #         if s_[-2] == '2':
        #             count *= dp[len(s_) - 2]
        #         else:
        #             count *= dp[len(s_) - 1]
        #     else:
        #         if len(s_) > 2:
        #             count *= dp[len(s_) - 2] + dp[len(s_) - 3]
        #         else:
        #             count *= dp[1]
        #
        # return count
