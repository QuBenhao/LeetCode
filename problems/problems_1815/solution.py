import solution
from functools import lru_cache


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.maxHappyGroups(*test_input)

    def maxHappyGroups(self, batchSize, groups):
        """
        :type batchSize: int
        :type groups: List[int]
        :rtype: int
        """
        remains = [0] * batchSize
        for g in groups:
            remains[g % batchSize] += 1
        ans = remains[0]
        remains[0] = 0
        # Greedy: pair remainders that sum to batchSize
        for i in range(1, batchSize // 2 + 1):
            if i != batchSize - i:
                tp = min(remains[i], remains[batchSize - i])
                ans += tp
                remains[i] -= tp
                remains[batchSize - i] -= tp
            # Middle remainder
            else:
                ans += remains[i] // 2
                remains[i] %= 2

        # Remainder of the previous total and the remaining groups
        @lru_cache(None)
        def dfs(s, remain):
            res = 0
            for i in range(1, batchSize):
                # Groups with remainder i modulo batchSize remain
                if remain[i-1]:
                    r = list(remain)
                    r[i-1] -= 1
                    # If the previous total has remainder 0, add 1 happy group to the DFS result; otherwise, use the DFS result
                    res = max(res, (s == 0) + dfs((s+i) % batchSize, tuple(r)))
            # Do not add (s==0) here because remain may already be empty
            return res

        return ans + dfs(0, tuple(remains[1:]))
