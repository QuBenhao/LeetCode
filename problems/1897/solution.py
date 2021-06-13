import solution
from collections import Counter


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.makeEqual(list(test_input))

    def makeEqual(self, words):
        """
        :type words: List[str]
        :rtype: bool
        """
        counter = Counter()
        for w in words:
            for c in w:
                counter[c] += 1
        return all(v % len(words) == 0 for v in counter.values())
