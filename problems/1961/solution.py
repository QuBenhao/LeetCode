import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        s, words = test_input
        return self.isPrefixString(str(s), list(words))

    def isPrefixString(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: bool
        """
        n = len(s)
        cur = ""
        for word in words:
            if len(cur) < n:
                cur += word
            else:
                break
        return s == cur
