import solution
from collections import Counter


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.frequencySort(str(test_input))

    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        return "".join(char * repeats for char,repeats in sorted(Counter(s).items(), key=lambda x:(-x[1],ord(x[0]))))
