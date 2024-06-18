import solution
from itertools import pairwise


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.romanToInt(str(test_input))

    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman_dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        ans = roman_dict[s[0]]
        for last, cur in pairwise(s):
            if (ld := roman_dict[last]) < (cd := roman_dict[cur]):
                ans += cd - 2 * ld
            else:
                ans += cd
        return ans
