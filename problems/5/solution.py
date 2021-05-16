import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.longestPalindrome(str(test_input))

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        T = '$#' + '#'.join(s) + '#@'
        l = len(T)
        P = [0] * l
        R, C, ans = 0, 0, s[0]
        for i in range(1, l - 1):
            if i < R:
                P[i] = min(P[2 * C - i], R - i)

            while T[i + (P[i] + 1)] == T[i - (P[i] + 1)]:
                P[i] += 1

            if P[i] + i > R:
                R = P[i] + i
                C = i

            if P[i] > len(ans):
                index = (i - 2) // 2
                length = P[i] // 2
                if i % 2 == 0:
                    ans = s[index - length:index + length + 1]
                else:
                    ans = s[index - length + 1:index + length + 1]
        return ans

        # lenS = len(s)
        # if lenS <= 1:
        #     return s
        # minStart, maxLen, i = 0, 1, 0
        # while i < lenS:
        #     if lenS - i <= maxLen / 2:
        #         break
        #     j, k = i, i
        #     while k < lenS - 1 and s[k] == s[k + 1]:
        #         k += 1
        #     i = k + 1
        #     while k < lenS - 1 and j and s[k + 1] == s[j - 1]:
        #         k, j = k + 1, j - 1
        #     if k - j + 1 > maxLen:
        #         minStart, maxLen = j, k - j + 1
        # return s[minStart: minStart + maxLen]

        # import collections
        #
        # def is_palindrome(string):
        #     return string[::-1] == string
        #
        # n = len(s)
        # ans = s[0]
        # index_dict = collections.defaultdict(list)
        # for i in range(n):
        #     for index in index_dict[s[i]]:
        #         if i - index + 1 <= len(ans):
        #             break
        #         elif is_palindrome(s[index:i+1]):
        #             ans = s[index:i+1]
        #             break
        #     index_dict[s[i]].append(i)
        # return ans
