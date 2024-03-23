import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.removeOccurrences(*test_input)

    def removeOccurrences(self, s, part):
        """
        :type s: str
        :type part: str
        :rtype: str
        """
        while part in s:
            idx = s.index(part)
            s = s[:idx] + s[idx+len(part):]
        return s
