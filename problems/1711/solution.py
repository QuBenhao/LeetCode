import solution
from collections import Counter


class Solution(solution.Solution):
    powersOfTwo = [2 ** i for i in range(22)]
    mod = 10 ** 9 + 7

    def solve(self, test_input=None):
        return self.countPairs(list(test_input))

    def countPairs(self, deliciousness):
        """
        :type deliciousness: List[int]
        :rtype: int
        """
        cnts = Counter(deliciousness)
        return (sum(
            cnts[key] * (cnts[key] - 1) if key == target - key else cnts[key] * cnts[target - key]
            for key in cnts for target in self.powersOfTwo)) // 2 % self.mod
