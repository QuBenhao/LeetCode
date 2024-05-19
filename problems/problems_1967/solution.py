import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.numOfStrings(*test_input)

    def numOfStrings(self, patterns, word):
        """
        :type patterns: List[str]
        :type word: str
        :rtype: int
        """
        return sum(p in word for p in patterns)
