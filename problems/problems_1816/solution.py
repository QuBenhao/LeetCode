import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.truncateSentence(*test_input)

    def truncateSentence(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        return " ".join(s.split(" ")[:k])
