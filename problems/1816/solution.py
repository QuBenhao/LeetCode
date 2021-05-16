import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        s, k = test_input
        return self.truncateSentence(str(s), k)

    def truncateSentence(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        return " ".join(s.split(" ")[:k])
