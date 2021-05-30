import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        firstWord, secondWord, targetWord = test_input
        return self.isSumEqual(str(firstWord), str(secondWord), str(targetWord))

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
