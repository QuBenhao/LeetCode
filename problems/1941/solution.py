import solution
from collections import Counter


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.areOccurrencesEqual(str(test_input))

    def areOccurrencesEqual(self, s):
        """
        :type s: str
        :rtype: bool
        """
        return len(set(Counter(s).values())) == 1
