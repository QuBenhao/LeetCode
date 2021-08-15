import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        patterns, word = test_input
        return self.numOfStrings(list(patterns), str(word))

    def numOfStrings(self, patterns, word):
        """
        :type patterns: List[str]
        :type word: str
        :rtype: int
        """
        return sum(1 for p in patterns if p in word)
