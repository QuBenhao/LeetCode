import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.titleToNumber(str(test_input))

    def titleToNumber(self, columnTitle):
        """
        :type columnTitle: str
        :rtype: int
        """
        ans = 0
        for c in columnTitle:
            ans = 26 * ans + (ord(c) - ord('A') + 1)
        return ans
