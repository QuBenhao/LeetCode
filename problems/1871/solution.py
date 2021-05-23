import solution
import re
from functools import lru_cache


class Solution(solution.Solution):
    def solve(self, test_input=None):
        s, minJump, maxJump = test_input
        return self.canReach(str(s), minJump, maxJump)

    def canReach(self, s, minJump, maxJump):
        """
        :type s: str
        :type minJump: int
        :type maxJump: int
        :rtype: bool
        """
        @lru_cache(None)
        def dfs(i):
            if i == n - 1:
                return True
            if s[i] == '1' or n - 1 - i < minJump:
                return False
            for j in range(min(i+maxJump,n-1), i+minJump-1,-1):
                if dfs(j):
                    return True
            return False

        if s[-1] == '1':
            return False
        if len(max(re.split('0+',s),key=len)) >= maxJump:
            return False
        n = len(s)
        return dfs(0)
