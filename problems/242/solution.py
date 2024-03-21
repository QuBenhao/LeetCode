import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.isAnagram(*test_input)

    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if set(s) == set(t):
            for c in set(s):
                if s.count(c) != t.count(c):
                    return False
            return True
        return False
