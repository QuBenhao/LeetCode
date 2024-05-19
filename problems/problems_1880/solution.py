import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.isSumEqual(*test_input)

    def isSumEqual(self, firstWord, secondWord, targetWord):
        """
        :type firstWord: str
        :type secondWord: str
        :type targetWord: str
        :rtype: bool
        """
        def helper(s):
            res = 0
            for c in s:
                res = 10 * res + ord(c) - ord('a')
            return res

        return helper(firstWord) + helper(secondWord) == helper(targetWord)
