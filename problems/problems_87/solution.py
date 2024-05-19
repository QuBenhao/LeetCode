import solution
import functools


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.isScramble(*test_input)

    @functools.lru_cache(None)
    def isScramble(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if sorted(s1) != sorted(s2):
            return False
        if s1 == s2:
            return True
        for i in range(1,len(s1)):
            # x,i,y
            if self.isScramble(s1[:i], s2[:i]) and self.isScramble(s1[i:],s2[i:]):
                return True
            # y,i,x
            if self.isScramble(s1[:i], s2[-i:]) and self.isScramble(s1[i:],s2[:-i]):
                return True
        return False
