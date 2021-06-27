import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.removeOccurrences(str(test_input[0]), str(test_input[1]))

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
