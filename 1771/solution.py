import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        word1, word2 = test_input
        return self.longestPalindrome(str(word1), str(word2))

    def longestPalindrome(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
