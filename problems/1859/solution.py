import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.sortSentence(str(test_input))

    def sortSentence(self, s):
        """
        :type s: str
        :rtype: str
        """
        return " ".join(c[:-1] for c in sorted(s.split(" "), key=lambda x:x[-1]))
