import solution
from collections import deque


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.countGoodSubstrings(str(test_input))

    def countGoodSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        window = deque([])
        ans = 0
        for c in s:
            window.append(c)
            if len(window) == 3:
                if len(set(window)) == 3:
                    ans += 1
                window.popleft()
        return ans
