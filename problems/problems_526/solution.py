import solution
from collections import defaultdict
from functools import lru_cache


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.countArrangement(test_input)

    def countArrangement(self, n):
        """
        :type n: int
        :rtype: int
        """
        canFill = defaultdict(list)
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                # Numbers that can be placed at each position
                if j % i == 0 or i % j == 0:
                    canFill[i].append(j - 1)
        # Sort by the number of choices and fill the positions with fewer choices first
        order = sorted(canFill.keys(), key=lambda x: len(canFill[x]))
        end = (1 << n) - 1

        @lru_cache(None)
        def dfs(state):
            # All positions are filled
            if state == end:
                return 1
            cnts = ans = 0
            # The position to fill next
            for i in range(n):
                if (1 << i) & state:
                    cnts += 1
            # Numbers allowed at the current position
            for i in canFill[order[cnts]]:
                # Numbers not yet used
                if not ((1 << i) & state):
                    ans += dfs(state ^ (1 << i))
            return ans

        return dfs(0)
