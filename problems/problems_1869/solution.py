import solution
import re


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.checkZeroOnes(str(test_input))

    def checkZeroOnes(self, s):
        """
        :type s: str
        :rtype: bool
        """
        l1 = re.split("0+", s)
        l0 = re.split("1+", s)
        return len(max(l1, key=len)) > len(max(l0, key=len))
